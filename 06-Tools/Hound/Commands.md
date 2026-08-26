# Hound - Commands

This file contains the commands that I used while learning and testing Hound in my personal cybersecurity lab.

---

# Navigate to Hound Directory

```bash
cd ~/CyberTools/hound
```

Purpose:

Move to the Hound project directory.

---

# List Files

```bash
ls -l
```

Purpose:

Display all files and their permissions.

---

# Start Hound

```bash
bash hound.sh
```

Purpose:

Launch the Hound tool.

---

# Start PHP Server Manually

```bash
php -S 127.0.0.1:8080
```

Purpose:

Start a local PHP web server.

---

# Check Running Processes

```bash
ps aux | grep cloudflared
```

Purpose:

Verify whether Cloudflared is running.

---

# Display Cloudflare Logs

```bash
cat cf.log
```

Purpose:

Read Cloudflared log messages.

Useful for:

- Tunnel URL
- Errors
- Connection status

---

# Check Listening Ports

```bash
ss -tlnp
```

Purpose:

Display TCP ports currently listening.

---

# Show Specific Ports

```bash
ss -tlnp | grep -E "3333|8080"
```

Purpose:

Check whether Hound or PHP server is listening on ports 3333 or 8080.

---

# Display Current Directory

```bash
pwd
```

Purpose:

Print the current working directory.

---

# Show Directory Structure

```bash
tree .
```

Purpose:

Display the folder structure.

---

# Display File Contents

```bash
cat data.txt
```

Purpose:

View captured data.

---

# Stop Running Process

```bash
Ctrl + C
```

Purpose:

Stop the currently running PHP server or Hound process.

---

# My Learning

While using these commands, I learned:

- How to host a local PHP server.
- How to verify whether Cloudflared is running.
- How to inspect log files.
- How to check listening ports.
- Basic Linux troubleshooting commands.
