# Hound - Errors

This document contains the problems that I encountered while learning Hound in my personal cybersecurity lab and how I solved them.

---

# Error 1

## Problem

Cloudflare Tunnel started but no public URL was displayed.

### Symptoms

- Hound kept waiting.
- No `trycloudflare.com` link appeared.

### Possible Causes

- Cloudflared was not running correctly.
- Internet connection problem.
- Cloudflare service issue.

### Commands Used

```bash
ps aux | grep cloudflared
```

```bash
cat cf.log
```

### Solution

- Verified that cloudflared was running.
- Checked the log file.
- Restarted Hound.
- Started a new tunnel.

### Result

Public URL was generated successfully.

---

# Error 2

## Problem

Cloudflare Tunnel stopped immediately after starting.

### Symptoms

Tunnel exited after a few seconds.

### Command Used

```bash
cat cf.log
```

### Cause

The local PHP server was not running, so Cloudflare had nothing to forward.

### Solution

Restarted the PHP server and then started Cloudflare Tunnel again.

### Result

Tunnel stayed active.

---

# Error 3

## Problem

No GPS Location Received.

### Symptoms

Output showed:

Location Unavailable

### Cause

Browser location permission was denied or not granted.

### Solution

Allowed location permission in the browser.

### Result

GPS coordinates were displayed.

---

# Error 4

## Problem

Only localhost was working.

### Symptoms

The page opened on the laptop but not on the phone.

### Cause

Localhost (127.0.0.1) is only accessible from the same machine.

### Solution

Started Hound with Cloudflare Tunnel.

### Result

The page became accessible from another device using the temporary public URL.

---

# Error 5

## Problem

Cloudflare link changed every time.

### Cause

Quick Tunnels are temporary.

### Solution

This is expected behavior. Each new session creates a new URL.

---

# Error 6

## Problem

Browser information was incomplete.

### Symptoms

Some fields displayed:

RAM: undefined

### Cause

Not all browsers expose the same information through browser APIs.

### Solution

No action required.

This depends on the browser.

---

# Error 7

## Problem

Cloudflared process was already running.

### Symptoms

Unexpected behavior while starting a new tunnel.

### Command Used

```bash
ps aux | grep cloudflared
```

### Solution

Stopped the existing process and restarted the tool.

---

# Lessons Learned

During testing I learned:

- Read log files before guessing.
- Check whether services are running.
- Verify listening ports.
- Browser permissions affect collected data.
- Localhost and public URLs behave differently.
- Temporary Cloudflare URLs change between sessions.

---

# Conclusion

Most issues were caused by:

- Browser permissions
- Local server status
- Cloudflare Tunnel state
- Network configuration

Systematic troubleshooting made the problems easier to identify and resolve.
