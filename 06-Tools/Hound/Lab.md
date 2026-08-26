# Hound - Lab

## Lab Information

**Tool:** Hound

**Developer:** TechChip

**Operating System:** Kali Linux 2026

**Test Environment:** Personal Cybersecurity Lab

**Devices Used:**

- Personal Laptop
- Personal Android Phone (Android 15)

---

# Lab Objective

The objective of this lab was to understand how Hound works for browser-based information gathering and to learn the difference between localhost and Cloudflare Tunnel.

---

# Lab 1 - Running Hound on Localhost

## Goal

Run Hound locally and access it from the same computer.

### Steps

1. Open Terminal.
2. Go to the Hound directory.

```bash
cd ~/CyberTools/hound
```

3. Start the tool.

```bash
bash hound.sh
```

4. Select:

```
Cloudflare Tunnel : No
```

5. Open:

```
http://127.0.0.1:8080
```

in the browser.

### Observation

- PHP server started successfully.
- Browser page loaded.
- Device information was displayed.
- Public IP information was shown.
- GPS was unavailable until location permission was granted.

### Result

Localhost mode worked successfully.

---

# Lab 2 - Cloudflare Tunnel

## Goal

Access Hound from another personal device.

### Steps

1. Start Hound.
2. Enable Cloudflare Tunnel.
3. Wait for the tunnel to start.
4. Copy the generated URL.
5. Open the URL on my Android phone.

### Observation

- Cloudflare generated a temporary public URL.
- The page opened successfully on my phone.
- Browser requested location permission.
- After allowing permission, GPS coordinates were displayed.

### Result

Cloudflare Tunnel worked successfully.

---

# Lab 3 - Browser Information Collection

### Information Observed

- Browser Name
- Browser Language
- User Agent
- Screen Resolution
- CPU Cores
- RAM (if available)
- Cookies Enabled

### Observation

Different browsers may expose different information.

---

# Lab 4 - IP Information

### Information Collected

- Public IP
- ISP
- Country
- State
- City

### Observation

This information was approximate and based on the public IP address.

---

# Lab 5 - GPS Permission

### Test

Opened the page and allowed location permission.

### Observation

After permission was granted:

- Latitude was displayed.
- Longitude was displayed.
- Google Maps link was generated.

### Result

GPS worked only after permission was granted.

---

# Commands Used

```bash
bash hound.sh
```

```bash
ps aux | grep cloudflared
```

```bash
cat cf.log
```

```bash
ss -tlnp
```

```bash
ls -l
```

---

# What I Learned

During this lab I learned:

- How localhost works.
- How a PHP server hosts a webpage.
- How Cloudflare Tunnel exposes a local server.
- Difference between IP location and GPS location.
- Importance of browser permissions.
- Basic troubleshooting using Linux commands.

---

# Final Result

The lab was completed successfully using my own laptop and Android phone in a controlled environment. I gained practical experience with local hosting, Cloudflare Tunnel, browser permissions, and information gathering concepts.
