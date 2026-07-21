# Linux Commands Notes
## Part 2 - File Permissions, Users & Groups (51-100)

---

# 51. id
## Description
Displays user ID (UID), group ID (GID), and groups.

```bash
id
```

---

# 52. groups
## Description
Shows the groups of the current user.

```bash
groups
```

---

# 53. users
## Description
Displays currently logged-in users.

```bash
users
```

---

# 54. who
## Description
Shows who is logged into the system.

```bash
who
```

---

# 55. w
## Description
Shows logged-in users and what they are doing.

```bash
w
```

---

# 56. last
## Description
Displays login history.

```bash
last
```

---

# 57. sudo
## Description
Run a command with administrator privileges.

```bash
sudo apt update
```

---

# 58. su
## Description
Switch to another user.

```bash
su username
```

---

# 59. passwd
## Description
Change the current user's password.

```bash
passwd
```

---

# 60. useradd
## Description
Create a new user.

```bash
sudo useradd username
```

---

# 61. adduser
## Description
Create a new user interactively.

```bash
sudo adduser username
```

---

# 62. userdel
## Description
Delete a user account.

```bash
sudo userdel username
```

---

# 63. userdel -r
## Description
Delete a user along with the home directory.

```bash
sudo userdel -r username
```

---

# 64. groupadd
## Description
Create a new group.

```bash
sudo groupadd developers
```

---

# 65. groupdel
## Description
Delete a group.

```bash
sudo groupdel developers
```

---

# 66. usermod
## Description
Modify a user account.

```bash
sudo usermod username
```

---

# 67. usermod -aG
## Description
Add a user to a group.

```bash
sudo usermod -aG sudo username
```

---

# 68. chgrp
## Description
Change the group ownership of a file.

```bash
chgrp developers file.txt
```

---

# 69. chmod 755
## Description
Set permissions to rwxr-xr-x.

```bash
chmod 755 file.sh
```

---

# 70. chmod 644
## Description
Set permissions to rw-r--r--.

```bash
chmod 644 file.txt
```

---

# 71. chmod +x
## Description
Make a file executable.

```bash
chmod +x script.sh
```

---

# 72. chmod -x
## Description
Remove execute permission.

```bash
chmod -x script.sh
```

---

# 73. chmod u+x
## Description
Give execute permission to the owner.

```bash
chmod u+x script.sh
```

---

# 74. chmod g+w
## Description
Give write permission to the group.

```bash
chmod g+w file.txt
```

---

# 75. chmod o-r
## Description
Remove read permission from others.

```bash
chmod o-r secret.txt
```

---

# 76. chmod a+r
## Description
Give read permission to everyone.

```bash
chmod a+r notes.txt
```

---

# 77. chmod -R
## Description
Change permissions recursively.

```bash
chmod -R 755 project/
```

---

# 78. stat
## Description
Display detailed file information.

```bash
stat file.txt
```

---

# 79. umask
## Description
Show default file permissions.

```bash
umask
```

---

# 80. umask 022
## Description
Set default permission mask.

```bash
umask 022
```

---

# 81. ln
## Description
Create a hard link.

```bash
ln file.txt hardlink.txt
```

---

# 82. ln -s
## Description
Create a symbolic link.

```bash
ln -s file.txt shortcut.txt
```

---

# 83. readlink
## Description
Display the target of a symbolic link.

```bash
readlink shortcut.txt
```

---

# 84. file
## Description
Identify the file type.

```bash
file image.png
```

---

# 85. basename
## Description
Extract the filename from a path.

```bash
basename /home/user/file.txt
```

---

# 86. dirname
## Description
Extract the directory path.

```bash
dirname /home/user/file.txt
```

---

# 87. realpath
## Description
Display the absolute path.

```bash
realpath file.txt
```

---

# 88. tree
## Description
Display directories in a tree format.

```bash
tree
```

---

# 89. lsattr
## Description
Display file attributes.

```bash
lsattr file.txt
```

---

# 90. chattr
## Description
Change file attributes.

```bash
sudo chattr +i file.txt
```

---

# 91. getfacl
## Description
View Access Control List (ACL).

```bash
getfacl file.txt
```

---

# 92. setfacl
## Description
Set Access Control List (ACL).

```bash
setfacl -m u:username:rwx file.txt
```

---

# 93. install
## Description
Copy files and set permissions.

```bash
install script.sh /usr/local/bin/
```

---

# 94. cp -r
## Description
Copy directories recursively.

```bash
cp -r source destination
```

---

# 95. mv -i
## Description
Move files with confirmation.

```bash
mv -i file.txt backup/
```

---

# 96. rm -i
## Description
Delete files with confirmation.

```bash
rm -i file.txt
```

---

# 97. shred
## Description
Securely overwrite and delete a file.

```bash
shred -u secret.txt
```

---

# 98. sync
## Description
Flush filesystem buffers to disk.

```bash
sync
```

---

# 99. sync && reboot
## Description
Sync data and reboot the system.

```bash
sync && reboot
```

---

# 100. sync && poweroff
## Description
Sync data and safely shut down the system.

```bash
sync && poweroff
```

---
