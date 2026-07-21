# Linux Commands Notes
## Part 5 - Process Management Commands (201-250)

---

# 201. ps
## Description
Display information about currently running processes.

```bash
ps
```

---

# 202. ps -e
## Description
Display all running processes.

```bash
ps -e
```

---

# 203. ps -ef
## Description
Display all running processes in full format.

```bash
ps -ef
```

---

# 204. ps aux
## Description
Display detailed information about all processes.

```bash
ps aux
```

---

# 205. top
## Description
Display real-time system processes.

```bash
top
```

---

# 206. htop
## Description
Interactive process viewer.

```bash
htop
```

---

# 207. btop
## Description
Modern resource monitor.

```bash
btop
```

---

# 208. pidof
## Description
Find the Process ID (PID) of a program.

```bash
pidof firefox
```

---

# 209. pgrep
## Description
Search for processes by name.

```bash
pgrep ssh
```

---

# 210. pstree
## Description
Display processes as a tree.

```bash
pstree
```

---

# 211. kill
## Description
Terminate a process using its PID.

```bash
kill 1234
```

---

# 212. kill -9
## Description
Forcefully terminate a process.

```bash
kill -9 1234
```

---

# 213. killall
## Description
Kill all processes with a given name.

```bash
killall firefox
```

---

# 214. pkill
## Description
Terminate processes by name.

```bash
pkill firefox
```

---

# 215. xkill
## Description
Kill a graphical application by clicking on it.

```bash
xkill
```

---

# 216. jobs
## Description
Display background jobs.

```bash
jobs
```

---

# 217. bg
## Description
Resume a suspended job in the background.

```bash
bg
```

---

# 218. fg
## Description
Bring a background job to the foreground.

```bash
fg
```

---

# 219. nohup
## Description
Run a command that continues after logout.

```bash
nohup python3 app.py &
```

---

# 220. &
## Description
Run a command in the background.

```bash
python3 app.py &
```

---

# 221. nice
## Description
Start a process with a specified priority.

```bash
nice -n 10 python3 app.py
```

---

# 222. renice
## Description
Change the priority of a running process.

```bash
sudo renice 5 -p 1234
```

---

# 223. watch
## Description
Run a command repeatedly.

```bash
watch -n 2 free -h
```

---

# 224. time
## Description
Measure the execution time of a command.

```bash
time ls
```

---

# 225. timeout
## Description
Run a command with a time limit.

```bash
timeout 10 ping google.com
```

---

# 226. sleep
## Description
Pause execution for a specified time.

```bash
sleep 5
```

---

# 227. uptime
## Description
Display system uptime.

```bash
uptime
```

---

# 228. vmstat
## Description
Display virtual memory statistics.

```bash
vmstat
```

---

# 229. iostat
## Description
Display CPU and disk I/O statistics.

```bash
iostat
```

---

# 230. mpstat
## Description
Display CPU usage statistics.

```bash
mpstat
```

---

# 231. sar
## Description
Collect and display system activity.

```bash
sar
```

---

# 232. dstat
## Description
Display system resource statistics.

```bash
dstat
```

---

# 233. free
## Description
Display memory usage.

```bash
free
```

---

# 234. free -h
## Description
Display memory usage in human-readable format.

```bash
free -h
```

---

# 235. lscpu
## Description
Display CPU information.

```bash
lscpu
```

---

# 236. lsmem
## Description
Display memory information.

```bash
lsmem
```

---

# 237. lsblk
## Description
List block storage devices.

```bash
lsblk
```

---

# 238. ulimit -a
## Description
Display user resource limits.

```bash
ulimit -a
```

---

# 239. systemd-cgls
## Description
Display systemd control groups.

```bash
systemd-cgls
```

---

# 240. systemd-cgtop
## Description
Display resource usage by control groups.

```bash
systemd-cgtop
```

---

# 241. loginctl
## Description
Display active user sessions.

```bash
loginctl
```

---

# 242. loginctl list-sessions
## Description
List all active sessions.

```bash
loginctl list-sessions
```

---

# 243. journalctl
## Description
View system logs.

```bash
journalctl
```

---

# 244. journalctl -xe
## Description
View detailed error logs.

```bash
journalctl -xe
```

---

# 245. journalctl -f
## Description
Follow logs in real time.

```bash
journalctl -f
```

---

# 246. dmesg
## Description
Display kernel ring buffer messages.

```bash
dmesg
```

---

# 247. dmesg -T
## Description
Display kernel logs with human-readable timestamps.

```bash
dmesg -T
```

---

# 248. strace
## Description
Trace system calls made by a process.

```bash
strace ls
```

---

# 249. ltrace
## Description
Trace library calls made by a program.

```bash
ltrace ls
```

---

# 250. perf
## Description
Analyze Linux system and application performance.

```bash
perf stat ls
```

---
