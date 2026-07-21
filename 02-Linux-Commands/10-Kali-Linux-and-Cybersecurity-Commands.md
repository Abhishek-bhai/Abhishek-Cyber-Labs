# Linux Commands Notes
## Part 10 - Kali Linux and Cybersecurity Commands (451-500)

---

# Section 1 - Reconnaissance & Scanning

---

# 451. nmap

## Description
Scan a target host for open ports.

```bash
nmap 192.168.1.10
```

---

# 452. nmap -sS

## Description
Perform a TCP SYN (Stealth) scan.

```bash
sudo nmap -sS 192.168.1.10
```

---

# 453. nmap -sV

## Description
Detect service versions.

```bash
nmap -sV 192.168.1.10
```

---

# 454. nmap -O

## Description
Detect the target operating system.

```bash
sudo nmap -O 192.168.1.10
```

---

# 455. nmap -A

## Description
Run aggressive scan (OS, Version, Scripts, Traceroute).

```bash
sudo nmap -A 192.168.1.10
```

---

# 456. nmap -Pn

## Description
Treat the target as online.

```bash
nmap -Pn 192.168.1.10
```

---

# 457. nmap -p

## Description
Scan specific ports.

```bash
nmap -p 22,80,443 192.168.1.10
```

---

# 458. nmap -p-

## Description
Scan all 65535 TCP ports.

```bash
nmap -p- 192.168.1.10
```

---

# 459. nmap -sn

## Description
Perform host discovery only.

```bash
nmap -sn 192.168.1.0/24
```

---

# 460. nmap --script

## Description
Run NSE scripts.

```bash
nmap --script vuln 192.168.1.10
```

---

# 461. nmap -oN

## Description
Save scan results in normal format.

```bash
nmap -oN scan.txt 192.168.1.10
```

---

# 462. nmap -oX

## Description
Save scan results in XML format.

```bash
nmap -oX scan.xml 192.168.1.10
```

---

# 463. nmap -oA

## Description
Save scan results in all formats.

```bash
nmap -oA scan 192.168.1.10
```

---

# 464. masscan

## Description
High-speed port scanner.

```bash
sudo masscan 192.168.1.0/24 -p80
```

---

# 465. rustscan

## Description
Fast TCP port scanner.

```bash
rustscan -a 192.168.1.10
```

---

# 466. arp-scan

## Description
Discover hosts on the local network.

```bash
sudo arp-scan --localnet
```

---

# 467. netdiscover

## Description
Passive network discovery tool.

```bash
sudo netdiscover
```

---

# 468. fping

## Description
Ping multiple hosts.

```bash
fping -a -g 192.168.1.0/24
```

---

# 469. hping3

## Description
Craft and send custom TCP/IP packets.

```bash
sudo hping3 -S 192.168.1.10 -p 80
```

---

# 470. traceroute

## Description
Trace the network path to a host.

```bash
traceroute google.com
```

---

# Section 2 - DNS Enumeration

---

# 471. dig

## Description
Query DNS records.

```bash
dig example.com
```

---

# 472. host

## Description
Resolve DNS information.

```bash
host example.com
```

---

# 473. nslookup

## Description
Perform DNS lookup.

```bash
nslookup example.com
```

---

# 474. dnsenum

## Description
Enumerate DNS information.

```bash
dnsenum example.com
```

---

# 475. dnsrecon

## Description
DNS reconnaissance tool.

```bash
dnsrecon -d example.com
```

---

# 476. fierce

## Description
DNS reconnaissance utility.

```bash
fierce --domain example.com
```

---

# Section 3 - Web Reconnaissance

---

# 477. whatweb

## Description
Identify web technologies.

```bash
whatweb https://example.com
```

---

# 478. wafw00f

## Description
Detect Web Application Firewalls.

```bash
wafw00f https://example.com
```

---

# 479. nikto

## Description
Scan a web server for common vulnerabilities.

```bash
nikto -h https://example.com
```

---

# 480. gobuster dir

## Description
Brute-force directories.

```bash
gobuster dir -u https://example.com -w wordlist.txt
```

---

# 481. gobuster dns

## Description
Brute-force subdomains.

```bash
gobuster dns -d example.com -w wordlist.txt
```

---

# 482. ffuf

## Description
Fast web fuzzer.

```bash
ffuf -u https://example.com/FUZZ -w wordlist.txt
```

---

# 483. dirsearch

## Description
Discover hidden directories.

```bash
dirsearch -u https://example.com
```

---

# 484. feroxbuster

## Description
Recursive content discovery.

```bash
feroxbuster -u https://example.com
```

---

# 485. eyewitness

## Description
Capture screenshots of websites.

```bash
eyewitness --web
```

---

# Section 4 - Information Gathering

---

# 486. whois

## Description
Retrieve domain registration information.

```bash
whois example.com
```

---

# 487. theHarvester

## Description
Gather emails, subdomains and hosts.

```bash
theHarvester -d example.com -b bing
```

---

# 488. amass enum

## Description
Perform subdomain enumeration.

```bash
amass enum -d example.com
```

---

# 489. assetfinder

## Description
Find subdomains.

```bash
assetfinder example.com
```

---

# 490. subfinder

## Description
Passive subdomain discovery.

```bash
subfinder -d example.com
```

---

# 491. httpx

## Description
Probe live web servers.

```bash
httpx -l domains.txt
```

---

# 492. waybackurls

## Description
Retrieve archived URLs.

```bash
waybackurls example.com
```

---

# 493. gau

## Description
Fetch known URLs from multiple sources.

```bash
gau example.com
```

---

# 494. anew

## Description
Append only unique lines.

```bash
cat urls.txt | anew unique.txt
```

---

# 495. hakrawler

## Description
Crawl web applications.

```bash
hakrawler -url https://example.com
```

---

# 496. katana

## Description
Modern web crawler.

```bash
katana -u https://example.com
```

---

# 497. nuclei

## Description
Scan for known vulnerabilities using templates.

```bash
nuclei -u https://example.com
```

---

# 498. searchsploit

## Description
Search Exploit-DB locally.

```bash
searchsploit apache
```

---

# 499. curl -I

## Description
Retrieve only HTTP response headers.

```bash
curl -I https://example.com
```

---

# 500. wget --mirror

## Description
Mirror an entire website for offline analysis.

```bash
wget --mirror https://example.com
```

---



# Section 5 - Password Auditing & Enumeration

---

# 501. hydra

## Description
Login auditing tool that supports many network services.

```bash
hydra -L users.txt -P passwords.txt ssh://192.168.1.10
```

---

# 502. john

## Description
Password hash auditing tool.

```bash
john hashes.txt
```

---

# 503. john --wordlist

## Description
Use a custom wordlist with John.

```bash
john --wordlist=rockyou.txt hashes.txt
```

---

# 504. john --show

## Description
Display recovered passwords.

```bash
john --show hashes.txt
```

---

# 505. hashcat

## Description
GPU/CPU password hash auditing tool.

```bash
hashcat -m 0 hashes.txt rockyou.txt
```

---

# 506. hashcat --example-hashes

## Description
Display supported example hash formats.

```bash
hashcat --example-hashes
```

---

# 507. hashid

## Description
Identify hash types.

```bash
hashid hash.txt
```

---

# 508. hash-identifier

## Description
Identify common password hashes.

```bash
hash-identifier
```

---

# 509. cewl

## Description
Generate a custom wordlist from a website.

```bash
cewl https://example.com
```

---

# 510. crunch

## Description
Generate custom wordlists.

```bash
crunch 6 8 abc123
```

---

# Section 6 - SMB Enumeration

---

# 511. smbclient

## Description
Connect to SMB shares.

```bash
smbclient -L //192.168.1.10
```

---

# 512. smbmap

## Description
Enumerate SMB shares and permissions.

```bash
smbmap -H 192.168.1.10
```

---

# 513. enum4linux

## Description
Enumerate SMB and Samba information.

```bash
enum4linux 192.168.1.10
```

---

# 514. enum4linux-ng

## Description
Improved SMB enumeration tool.

```bash
enum4linux-ng 192.168.1.10
```

---

# 515. netexec

## Description
Network service enumeration framework.

```bash
netexec smb 192.168.1.10
```

---

# Section 7 - SQL Injection Testing

---

# 516. sqlmap

## Description
Automated SQL injection testing tool.

```bash
sqlmap -u "https://example.com?id=1"
```

---

# 517. sqlmap --dbs

## Description
Enumerate available databases.

```bash
sqlmap -u "https://example.com?id=1" --dbs
```

---

# 518. sqlmap --tables

## Description
List database tables.

```bash
sqlmap -u "https://example.com?id=1" -D database --tables
```

---

# 519. sqlmap --columns

## Description
List table columns.

```bash
sqlmap -u "https://example.com?id=1" -D database -T users --columns
```

---

# 520. sqlmap --dump

## Description
Export table contents.

```bash
sqlmap -u "https://example.com?id=1" -D database -T users --dump
```

---

# Section 8 - Network Services

---

# 521. ssh

## Description
Secure Shell remote login.

```bash
ssh user@192.168.1.10
```

---

# 522. scp

## Description
Securely copy files.

```bash
scp file.txt user@192.168.1.10:/home/user/
```

---

# 523. sftp

## Description
Secure file transfer.

```bash
sftp user@192.168.1.10
```

---

# 524. ftp

## Description
Connect to an FTP server.

```bash
ftp 192.168.1.10
```

---

# 525. telnet

## Description
Connect to a TCP service.

```bash
telnet 192.168.1.10 23
```

---

# 526. nc

## Description
Netcat networking utility.

```bash
nc 192.168.1.10 80
```

---

# 527. socat

## Description
Advanced networking utility.

```bash
socat TCP:192.168.1.10:80 STDOUT
```

---

# 528. rpcclient

## Description
Interact with Windows RPC services.

```bash
rpcclient -U "" -N 192.168.1.10
```

---

# 529. showmount

## Description
Display NFS exports.

```bash
showmount -e 192.168.1.10
```

---

# 530. rpcinfo

## Description
Display RPC service information.

```bash
rpcinfo -p 192.168.1.10
```

---

# Section 9 - Packet Analysis

---

# 531. wireshark

## Description
GUI packet analyzer.

```bash
wireshark
```

---

# 532. tshark

## Description
Command-line packet analyzer.

```bash
tshark
```

---

# 533. tcpdump

## Description
Capture network traffic.

```bash
sudo tcpdump -i eth0
```

---

# 534. tcpflow

## Description
Capture TCP data streams.

```bash
tcpflow
```

---

# 535. ngrep

## Description
Search packet payloads using patterns.

```bash
ngrep "HTTP"
```

---

# Section 10 - DNS & HTTP Testing

---

# 536. dnsx

## Description
Resolve and validate DNS records.

```bash
dnsx -l domains.txt
```

---

# 537. httprobe

## Description
Identify live HTTP services.

```bash
cat domains.txt | httprobe
```

---

# 538. httpie

## Description
User-friendly HTTP client.

```bash
http GET https://example.com
```

---

# 539. curl

## Description
Transfer data over HTTP/HTTPS.

```bash
curl https://example.com
```

---

# 540. wget

## Description
Download files via HTTP/HTTPS.

```bash
wget https://example.com/file.zip
```

---

# Section 11 - Utility Commands

---

# 541. file

## Description
Identify file type.

```bash
file sample.bin
```

---

# 542. strings

## Description
Extract printable strings from a binary.

```bash
strings sample.bin
```

---

# 543. xxd

## Description
Display a hexadecimal dump.

```bash
xxd sample.bin
```

---

# 544. hexdump

## Description
Display binary data in hexadecimal.

```bash
hexdump -C sample.bin
```

---

# 545. base64

## Description
Encode or decode Base64 data.

```bash
base64 file.txt
```

---

# 546. base64 -d

## Description
Decode Base64 data.

```bash
base64 -d encoded.txt
```

---

# 547. exiftool

## Description
Display file metadata.

```bash
exiftool image.jpg
```

---

# 548. binwalk

## Description
Analyze firmware images.

```bash
binwalk firmware.bin
```

---

# 549. foremost

## Description
Recover files from disk images.

```bash
foremost disk.img
```

---

# 550. bulk_extractor

## Description
Extract forensic artifacts from disk images.

```bash
bulk_extractor disk.img
```

---



