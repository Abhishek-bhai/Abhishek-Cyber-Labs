# Linux Commands Notes
## Part 4 - Package Management Commands (151-200)

---

# 151. apt update
## Description
Update the package list from repositories.

```bash
sudo apt update
```

---

# 152. apt upgrade
## Description
Upgrade installed packages.

```bash
sudo apt upgrade
```

---

# 153. apt full-upgrade
## Description
Upgrade packages including dependency changes.

```bash
sudo apt full-upgrade
```

---

# 154. apt install
## Description
Install a package.

```bash
sudo apt install nmap
```

---

# 155. apt remove
## Description
Remove an installed package.

```bash
sudo apt remove nmap
```

---

# 156. apt purge
## Description
Remove a package along with its configuration files.

```bash
sudo apt purge nmap
```

---

# 157. apt autoremove
## Description
Remove unused dependencies.

```bash
sudo apt autoremove
```

---

# 158. apt autoclean
## Description
Remove obsolete package files.

```bash
sudo apt autoclean
```

---

# 159. apt clean
## Description
Clear the local package cache.

```bash
sudo apt clean
```

---

# 160. apt search
## Description
Search for packages.

```bash
apt search wireshark
```

---

# 161. apt show
## Description
Display package information.

```bash
apt show nmap
```

---

# 162. apt list --installed
## Description
List installed packages.

```bash
apt list --installed
```

---

# 163. apt policy
## Description
Show installed and candidate versions.

```bash
apt policy nmap
```

---

# 164. apt-mark hold
## Description
Prevent a package from being upgraded.

```bash
sudo apt-mark hold firefox
```

---

# 165. apt-mark unhold
## Description
Allow upgrades again.

```bash
sudo apt-mark unhold firefox
```

---

# 166. dpkg -i
## Description
Install a .deb package.

```bash
sudo dpkg -i package.deb
```

---

# 167. dpkg -r
## Description
Remove a package.

```bash
sudo dpkg -r package_name
```

---

# 168. dpkg -l
## Description
List installed packages.

```bash
dpkg -l
```

---

# 169. dpkg -L
## Description
List files installed by a package.

```bash
dpkg -L nmap
```

---

# 170. dpkg -S
## Description
Find which package owns a file.

```bash
dpkg -S /usr/bin/nmap
```

---

# 171. dpkg --configure -a
## Description
Fix interrupted package installation.

```bash
sudo dpkg --configure -a
```

---

# 172. apt-cache search
## Description
Search package cache.

```bash
apt-cache search python
```

---

# 173. apt-cache depends
## Description
Show package dependencies.

```bash
apt-cache depends nmap
```

---

# 174. apt-cache show
## Description
Display package details.

```bash
apt-cache show curl
```

---

# 175. apt-cache policy
## Description
Show package version information.

```bash
apt-cache policy curl
```

---

# 176. add-apt-repository
## Description
Add a new software repository.

```bash
sudo add-apt-repository ppa:example/repo
```

---

# 177. apt edit-sources
## Description
Edit repository sources.

```bash
sudo apt edit-sources
```

---

# 178. cat /etc/apt/sources.list
## Description
View configured repositories.

```bash
cat /etc/apt/sources.list
```

---

# 179. nala update
## Description
Update packages using Nala.

```bash
sudo nala update
```

---

# 180. nala install
## Description
Install packages using Nala.

```bash
sudo nala install git
```

---

# 181. nala upgrade
## Description
Upgrade packages using Nala.

```bash
sudo nala upgrade
```

---

# 182. nala remove
## Description
Remove packages using Nala.

```bash
sudo nala remove git
```

---

# 183. snap list
## Description
List installed Snap packages.

```bash
snap list
```

---

# 184. snap install
## Description
Install a Snap package.

```bash
sudo snap install code
```

---

# 185. snap remove
## Description
Remove a Snap package.

```bash
sudo snap remove code
```

---

# 186. flatpak list
## Description
List installed Flatpak applications.

```bash
flatpak list
```

---

# 187. flatpak install
## Description
Install a Flatpak package.

```bash
flatpak install flathub org.mozilla.firefox
```

---

# 188. flatpak update
## Description
Update Flatpak packages.

```bash
flatpak update
```

---

# 189. flatpak uninstall
## Description
Remove a Flatpak package.

```bash
flatpak uninstall org.mozilla.firefox
```

---

# 190. aptitude
## Description
Interactive package manager.

```bash
sudo aptitude
```

---

# 191. deborphan
## Description
Find orphaned libraries.

```bash
deborphan
```

---

# 192. checkinstall
## Description
Create a .deb package from source installation.

```bash
sudo checkinstall
```

---

# 193. apt-file update
## Description
Update apt-file database.

```bash
sudo apt-file update
```

---

# 194. apt-file search
## Description
Find which package contains a file.

```bash
apt-file search ifconfig
```

---

# 195. apt download
## Description
Download a package without installing.

```bash
apt download nmap
```

---

# 196. apt reinstall
## Description
Reinstall a package.

```bash
sudo apt reinstall curl
```

---

# 197. apt satisfies
## Description
Check package dependency expressions.

```bash
apt satisfies "curl"
```

---

# 198. apt changelog
## Description
View a package changelog.

```bash
apt changelog git
```

---

# 199. apt moo
## Description
Hidden fun command in APT.

```bash
apt moo
```

---

# 200. apt --fix-broken install
## Description
Fix broken dependencies.

```bash
sudo apt --fix-broken install
```

---
