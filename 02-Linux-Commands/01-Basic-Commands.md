# Linux Commands Notes
## Part 1 - Basic Linux Commands (1-50)

---

# 1. pwd
## Description
Shows the current working directory.

## Syntax
```bash
pwd
```

Example:
```bash
pwd
```

---

# 2. ls
## Description
Lists files and directories.

```bash
ls
```

---

# 3. ls -l
## Description
Displays detailed information.

```bash
ls -l
```

---

# 4. ls -a
## Description
Shows hidden files.

```bash
ls -a
```

---

# 5. ls -la
## Description
Shows detailed information including hidden files.

```bash
ls -la
```

---

# 6. cd
## Description
Change directory.

```bash
cd folder_name
```

---

# 7. cd ..
## Description
Move one directory back.

```bash
cd ..
```

---

# 8. cd ~
## Description
Go to Home directory.

```bash
cd ~
```

---

# 9. clear
## Description
Clear terminal screen.

```bash
clear
```

---

# 10. whoami
## Description
Displays current username.

```bash
whoami
```

---

# 11. date
## Description
Displays current date and time.

```bash
date
```

---

# 12. cal
## Description
Shows calendar.

```bash
cal
```

---

# 13. uname
## Description
Shows operating system name.

```bash
uname
```

---

# 14. uname -a
## Description
Displays complete system information.

```bash
uname -a
```

---

# 15. hostname
## Description
Displays system hostname.

```bash
hostname
```

---

# 16. mkdir
## Description
Create a new directory.

```bash
mkdir test
```

---

# 17. rmdir
## Description
Remove an empty directory.

```bash
rmdir test
```

---

# 18. touch
## Description
Create an empty file.

```bash
touch file.txt
```

---

# 19. cp
## Description
Copy files.

```bash
cp file.txt backup.txt
```

---

# 20. mv
## Description
Move or rename files.

```bash
mv old.txt new.txt
```

---

# 21. rm
## Description
Delete a file.

```bash
rm file.txt
```

---

# 22. rm -r
## Description
Delete directory recursively.

```bash
rm -r folder
```

---

# 23. rm -rf
## Description
Force delete.

```bash
rm -rf folder
```

---

# 24. cat
## Description
Display file content.

```bash
cat file.txt
```

---

# 25. nano
## Description
Open Nano text editor.

```bash
nano file.txt
```

---

# 26. vim
## Description
Open Vim editor.

```bash
vim file.txt
```

---

# 27. less
## Description
Read large files.

```bash
less file.txt
```

---

# 28. head
## Description
Shows first 10 lines.

```bash
head file.txt
```

---

# 29. tail
## Description
Shows last 10 lines.

```bash
tail file.txt
```

---

# 30. tail -f
## Description
Monitor live logs.

```bash
tail -f logfile.log
```

---

# 31. echo
## Description
Print text.

```bash
echo "Hello Linux"
```

---

# 32. history
## Description
Shows command history.

```bash
history
```

---

# 33. man
## Description
Open manual page.

```bash
man ls
```

---

# 34. which
## Description
Shows executable path.

```bash
which python3
```

---

# 35. whereis
## Description
Locate binaries and manuals.

```bash
whereis python
```

---

# 36. find
## Description
Search files.

```bash
find . -name "*.py"
```

---

# 37. locate
## Description
Quickly find files.

```bash
locate file.txt
```

---

# 38. grep
## Description
Search text inside files.

```bash
grep "hello" file.txt
```

---

# 39. wc
## Description
Count lines, words, characters.

```bash
wc file.txt
```

---

# 40. sort
## Description
Sort lines.

```bash
sort file.txt
```

---

# 41. uniq
## Description
Remove duplicate lines.

```bash
uniq file.txt
```

---

# 42. chmod
## Description
Change file permissions.

```bash
chmod +x script.sh
```

---

# 43. chown
## Description
Change file owner.

```bash
sudo chown user:user file.txt
```

---

# 44. df -h
## Description
Shows disk usage.

```bash
df -h
```

---

# 45. du -sh
## Description
Shows directory size.

```bash
du -sh folder
```

---

# 46. free -h
## Description
Displays RAM usage.

```bash
free -h
```

---

# 47. top
## Description
Real-time system monitor.

```bash
top
```

---

# 48. htop
## Description
Interactive process monitor.

```bash
htop
```

---

# 49. ps
## Description
Shows running processes.

```bash
ps
```

---

# 50. kill
## Description
Terminate a process.

```bash
kill PID
```

---
