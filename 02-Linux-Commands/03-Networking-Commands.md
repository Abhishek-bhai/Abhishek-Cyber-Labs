# Linux Commands Notes
## Part 3 - Networking Commands (101-150)

---

# 101. ip addr
## Description
Displays IP addresses of all network interfaces.

```bash
ip addr
```

---

# 102. ip a
## Description
Short form of ip addr.

```bash
ip a
```

---

# 103. ip link
## Description
Displays network interfaces.

```bash
ip link
```

---

# 104. ip route
## Description
Shows routing table.

```bash
ip route
```

---

# 105. ip neigh
## Description
Displays ARP/Neighbor table.

```bash
ip neigh
```

---

# 106. hostname -I
## Description
Displays local IP address.

```bash
hostname -I
```

---

# 107. hostname -i
## Description
Displays host IP address.

```bash
hostname -i
```

---

# 108. ping
## Description
Checks connectivity to another host.

```bash
ping google.com
```

---

# 109. ping -c 4
## Description
Send only 4 ping packets.

```bash
ping -c 4 google.com
```

---

# 110. traceroute
## Description
Shows the path packets take to reach a destination.

```bash
traceroute google.com
```

---

# 111. tracepath
## Description
Trace packet route without root privileges.

```bash
tracepath google.com
```

---

# 112. mtr
## Description
Network diagnostic tool combining ping and traceroute.

```bash
mtr google.com
```

---

# 113. ss
## Description
Shows socket statistics.

```bash
ss
```

---

# 114. ss -tuln
## Description
Shows listening TCP and UDP ports.

```bash
ss -tuln
```

---

# 115. netstat
## Description
Displays network connections.

```bash
netstat
```

---

# 116. netstat -tulnp
## Description
Displays listening ports with process information.

```bash
sudo netstat -tulnp
```

---

# 117. lsof -i
## Description
Shows processes using network connections.

```bash
lsof -i
```

---

# 118. arp
## Description
Displays ARP cache.

```bash
arp -a
```

---

# 119. route
## Description
Displays routing table.

```bash
route -n
```

---

# 120. ifconfig
## Description
Displays network interface information (legacy).

```bash
ifconfig
```

---

# 121. iwconfig
## Description
Displays wireless interface information.

```bash
iwconfig
```

---

# 122. nmcli
## Description
Manage NetworkManager from terminal.

```bash
nmcli
```

---

# 123. curl
## Description
Transfer data from URLs.

```bash
curl https://example.com
```

---

# 124. curl -I
## Description
Fetch only HTTP headers.

```bash
curl -I https://google.com
```

---

# 125. wget
## Description
Download files from the internet.

```bash
wget https://example.com/file.zip
```

---

# 126. wget -c
## Description
Resume interrupted downloads.

```bash
wget -c https://example.com/file.zip
```

---

# 127. dig
## Description
DNS lookup tool.

```bash
dig google.com
```

---

# 128. nslookup
## Description
Query DNS records.

```bash
nslookup google.com
```

---

# 129. host
## Description
DNS lookup utility.

```bash
host google.com
```

---

# 130. ssh
## Description
Connect to a remote machine securely.

```bash
ssh user@192.168.1.10
```

---

# 131. ssh -p
## Description
Connect using a custom SSH port.

```bash
ssh -p 2222 user@192.168.1.10
```

---

# 132. scp
## Description
Securely copy files between systems.

```bash
scp file.txt user@192.168.1.10:/home/user/
```

---

# 133. scp -r
## Description
Copy directories securely.

```bash
scp -r project user@192.168.1.10:/home/user/
```

---

# 134. rsync
## Description
Synchronize files efficiently.

```bash
rsync -av source/ destination/
```

---

# 135. rsync -avz
## Description
Synchronize files with compression.

```bash
rsync -avz source/ user@server:/backup/
```

---

# 136. nc
## Description
Netcat for networking and debugging.

```bash
nc -lvnp 4444
```

---

# 137. telnet
## Description
Connect to remote TCP ports.

```bash
telnet google.com 80
```

---

# 138. ftp
## Description
Connect to an FTP server.

```bash
ftp ftp.example.com
```

---

# 139. sftp
## Description
Secure File Transfer Protocol.

```bash
sftp user@192.168.1.10
```

---

# 140. tcpdump
## Description
Capture network packets.

```bash
sudo tcpdump
```

---

# 141. tcpdump -i eth0
## Description
Capture packets on a specific interface.

```bash
sudo tcpdump -i eth0
```

---

# 142. nmap
## Description
Network discovery and port scanner.

```bash
nmap 192.168.1.1
```

---

# 143. nmap -sV
## Description
Detect service versions.

```bash
nmap -sV scanme.nmap.org
```

---

# 144. nmap -A
## Description
Aggressive scan.

```bash
sudo nmap -A scanme.nmap.org
```

---

# 145. nmap -O
## Description
Detect operating system.

```bash
sudo nmap -O target_ip
```

---

# 146. nmap -Pn
## Description
Treat host as online.

```bash
nmap -Pn target_ip
```

---

# 147. nmap -p
## Description
Scan specific ports.

```bash
nmap -p 22,80,443 target_ip
```

---

# 148. nmap -sn
## Description
Ping scan (host discovery only).

```bash
nmap -sn 192.168.1.0/24
```

---

# 149. nmap --script
## Description
Run NSE scripts.

```bash
nmap --script vuln target_ip
```

---

# 150. iperf3
## Description
Measure network bandwidth.

```bash
iperf3 -c server_ip
```

---
