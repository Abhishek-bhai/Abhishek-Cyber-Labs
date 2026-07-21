# Linux Commands Notes
## Part 9 - System Administration Commands (401-450)

---

# 401. systemctl

## Description
Manage systemd services.

```bash
sudo systemctl status ssh
```

---

# 402. systemctl start

## Description
Start a service.

```bash
sudo systemctl start apache2
```

---

# 403. systemctl stop

## Description
Stop a service.

```bash
sudo systemctl stop apache2
```

---

# 404. systemctl restart

## Description
Restart a service.

```bash
sudo systemctl restart apache2
```

---

# 405. systemctl reload

## Description
Reload a service configuration.

```bash
sudo systemctl reload nginx
```

---

# 406. systemctl enable

## Description
Enable a service at boot.

```bash
sudo systemctl enable ssh
```

---

# 407. systemctl disable

## Description
Disable a service at boot.

```bash
sudo systemctl disable apache2
```

---

# 408. systemctl is-active

## Description
Check whether a service is running.

```bash
systemctl is-active ssh
```

---

# 409. systemctl is-enabled

## Description
Check whether a service starts on boot.

```bash
systemctl is-enabled ssh
```

---

# 410. systemctl list-units

## Description
List active systemd units.

```bash
systemctl list-units
```

---

# 411. systemctl list-unit-files

## Description
List installed unit files.

```bash
systemctl list-unit-files
```

---

# 412. systemctl daemon-reload

## Description
Reload systemd configuration.

```bash
sudo systemctl daemon-reload
```

---

# 413. systemctl mask

## Description
Prevent a service from starting.

```bash
sudo systemctl mask apache2
```

---

# 414. systemctl unmask

## Description
Remove a service mask.

```bash
sudo systemctl unmask apache2
```

---

# 415. timedatectl

## Description
Display and manage system date and time.

```bash
timedatectl
```

---

# 416. timedatectl set-timezone

## Description
Change the system timezone.

```bash
sudo timedatectl set-timezone Asia/Kolkata
```

---

# 417. hostnamectl

## Description
Display system hostname information.

```bash
hostnamectl
```

---

# 418. hostnamectl set-hostname

## Description
Change the system hostname.

```bash
sudo hostnamectl set-hostname kali-linux
```

---

# 419. localectl

## Description
Display locale settings.

```bash
localectl
```

---

# 420. localectl set-locale

## Description
Set the system locale.

```bash
sudo localectl set-locale LANG=en_US.UTF-8
```

---

# 421. systemd-analyze

## Description
Analyze system boot performance.

```bash
systemd-analyze
```

---

# 422. systemd-analyze blame

## Description
Display boot time for services.

```bash
systemd-analyze blame
```

---

# 423. systemd-analyze critical-chain

## Description
Display boot dependency chain.

```bash
systemd-analyze critical-chain
```

---

# 424. crontab -e

## Description
Edit the current user's cron jobs.

```bash
crontab -e
```

---

# 425. crontab -l

## Description
List cron jobs.

```bash
crontab -l
```

---

# 426. crontab -r

## Description
Remove all cron jobs.

```bash
crontab -r
```

---

# 427. at

## Description
Schedule a one-time task.

```bash
at 10:00
```

---

# 428. atq

## Description
List pending at jobs.

```bash
atq
```

---

# 429. atrm

## Description
Remove an at job.

```bash
atrm 1
```

---

# 430. systemd-run

## Description
Run a command as a transient service.

```bash
systemd-run --on-active=5m echo "Hello"
```

---

# 431. sysctl

## Description
Display kernel parameters.

```bash
sysctl -a
```

---

# 432. sysctl -w

## Description
Modify a kernel parameter temporarily.

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

---

# 433. reboot

## Description
Restart the system.

```bash
sudo reboot
```

---

# 434. shutdown -h now

## Description
Shut down the system immediately.

```bash
sudo shutdown -h now
```

---

# 435. shutdown -r now

## Description
Restart the system immediately.

```bash
sudo shutdown -r now
```

---

# 436. poweroff

## Description
Power off the system.

```bash
sudo poweroff
```

---

# 437. halt

## Description
Stop the system.

```bash
sudo halt
```

---

# 438. wall

## Description
Send a message to all logged-in users.

```bash
wall "System maintenance starts in 5 minutes."
```

---

# 439. logger

## Description
Write a message to the system log.

```bash
logger "Backup completed successfully."
```

---

# 440. passwd -l

## Description
Lock a user account.

```bash
sudo passwd -l username
```

---

# 441. passwd -u

## Description
Unlock a user account.

```bash
sudo passwd -u username
```

---

# 442. chage -l

## Description
Display password aging information.

```bash
sudo chage -l username
```

---

# 443. chage

## Description
Modify password expiration settings.

```bash
sudo chage -M 90 username
```

---

# 444. visudo

## Description
Safely edit the sudoers file.

```bash
sudo visudo
```

---

# 445. hostnamectl status

## Description
Display detailed hostname information.

```bash
hostnamectl status
```

---

# 446. systemctl list-timers

## Description
List active systemd timers.

```bash
systemctl list-timers
```

---

# 447. systemctl cat

## Description
Display the contents of a unit file.

```bash
systemctl cat ssh.service
```

---

# 448. systemctl edit

## Description
Create or edit a systemd service override.

```bash
sudo systemctl edit ssh.service
```

---

# 449. systemctl show

## Description
Display detailed properties of a unit.

```bash
systemctl show ssh.service
```

---

# 450. systemctl status

## Description
Display the status of a service.

```bash
systemctl status apache2
```

---
