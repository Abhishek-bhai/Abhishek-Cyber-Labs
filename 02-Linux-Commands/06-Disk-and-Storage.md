# Linux Commands Notes
## Part 6 - Disk and Storage Commands (251-300)

---

# 251. df
## Description
Display filesystem disk space usage.

```bash
df
```

---

# 252. df -h
## Description
Display disk space usage in human-readable format.

```bash
df -h
```

---

# 253. df -T
## Description
Display filesystem type.

```bash
df -T
```

---

# 254. du
## Description
Estimate file and directory space usage.

```bash
du
```

---

# 255. du -h
## Description
Display directory size in human-readable format.

```bash
du -h
```

---

# 256. du -sh
## Description
Display the total size of a directory.

```bash
du -sh Downloads/
```

---

# 257. fdisk
## Description
Partition table manager.

```bash
sudo fdisk /dev/sdb
```

---

# 258. fdisk -l
## Description
List all disk partitions.

```bash
sudo fdisk -l
```

---

# 259. parted
## Description
Disk partitioning utility.

```bash
sudo parted /dev/sdb
```

---

# 260. cfdisk
## Description
Interactive partition editor.

```bash
sudo cfdisk /dev/sdb
```

---

# 261. blkid
## Description
Display block device attributes.

```bash
sudo blkid
```

---

# 262. findmnt
## Description
Display mounted filesystems.

```bash
findmnt
```

---

# 263. mount
## Description
Mount a filesystem.

```bash
sudo mount /dev/sdb1 /mnt
```

---

# 264. umount
## Description
Unmount a filesystem.

```bash
sudo umount /mnt
```

---

# 265. mount | grep
## Description
Check whether a filesystem is mounted.

```bash
mount | grep sdb1
```

---

# 266. mkfs.ext4
## Description
Create an Ext4 filesystem.

```bash
sudo mkfs.ext4 /dev/sdb1
```

---

# 267. mkfs.vfat
## Description
Create a FAT32 filesystem.

```bash
sudo mkfs.vfat /dev/sdb1
```

---

# 268. mkfs.ntfs
## Description
Create an NTFS filesystem.

```bash
sudo mkfs.ntfs /dev/sdb1
```

---

# 269. fsck
## Description
Check and repair a filesystem.

```bash
sudo fsck /dev/sdb1
```

---

# 270. e2fsck
## Description
Check an Ext filesystem.

```bash
sudo e2fsck /dev/sdb1
```

---

# 271. tune2fs
## Description
Modify Ext filesystem parameters.

```bash
sudo tune2fs -l /dev/sdb1
```

---

# 272. resize2fs
## Description
Resize an Ext filesystem.

```bash
sudo resize2fs /dev/sdb1
```

---

# 273. mkswap
## Description
Create swap space.

```bash
sudo mkswap /dev/sdb2
```

---

# 274. swapon
## Description
Enable swap space.

```bash
sudo swapon /dev/sdb2
```

---

# 275. swapoff
## Description
Disable swap space.

```bash
sudo swapoff /dev/sdb2
```

---

# 276. lsusb
## Description
List connected USB devices.

```bash
lsusb
```

---

# 277. lspci
## Description
List PCI devices.

```bash
lspci
```

---

# 278. lsdev
## Description
Display installed hardware devices.

```bash
lsdev
```

---

# 279. hwinfo
## Description
Display hardware information.

```bash
sudo hwinfo
```

---

# 280. lshw
## Description
Display hardware configuration.

```bash
sudo lshw
```

---

# 281. lsblk -f
## Description
Display filesystems on block devices.

```bash
lsblk -f
```

---

# 282. file -s
## Description
Determine filesystem type on a device.

```bash
sudo file -s /dev/sdb1
```

---

# 283. dd
## Description
Copy and convert files or disks.

```bash
sudo dd if=/dev/sda of=backup.img
```

---

# 284. shred
## Description
Securely overwrite a file.

```bash
shred secret.txt
```

---

# 285. sync
## Description
Flush filesystem buffers.

```bash
sync
```

---

# 286. tar
## Description
Create a tar archive.

```bash
tar -cvf archive.tar folder/
```

---

# 287. tar -xvf
## Description
Extract a tar archive.

```bash
tar -xvf archive.tar
```

---

# 288. tar -czvf
## Description
Create a compressed tar.gz archive.

```bash
tar -czvf backup.tar.gz folder/
```

---

# 289. tar -xzvf
## Description
Extract a tar.gz archive.

```bash
tar -xzvf backup.tar.gz
```

---

# 290. gzip
## Description
Compress a file.

```bash
gzip file.txt
```

---

# 291. gunzip
## Description
Extract a gzip archive.

```bash
gunzip file.txt.gz
```

---

# 292. zip
## Description
Create a ZIP archive.

```bash
zip archive.zip file.txt
```

---

# 293. unzip
## Description
Extract a ZIP archive.

```bash
unzip archive.zip
```

---

# 294. xz
## Description
Compress a file using XZ.

```bash
xz file.txt
```

---

# 295. unxz
## Description
Extract an XZ archive.

```bash
unxz file.txt.xz
```

---

# 296. zstd
## Description
Compress files using Zstandard.

```bash
zstd file.txt
```

---

# 297. unzstd
## Description
Extract Zstandard archives.

```bash
unzstd file.txt.zst
```

---

# 298. split
## Description
Split a large file into smaller files.

```bash
split -b 100M backup.iso part_
```

---

# 299. cat
## Description
Merge split files.

```bash
cat part_* > backup.iso
```

---

# 300. wipefs
## Description
Erase filesystem signatures from a device.

```bash
sudo wipefs -a /dev/sdb1
```

---
