# Hound - Notes

## What is Hound?

Hound is an information gathering tool developed by TechChip. It hosts a web page on a local PHP server or through a Cloudflare Tunnel. When a browser opens the page, the tool collects browser and device information. If the user grants permission, it can also access the device's GPS location.

---

# Learning Objectives

After using Hound, I learned:

- Difference between localhost and public URL
- How a PHP server works
- What Cloudflare Tunnel does
- How browser permissions work
- Difference between IP-based location and GPS location
- How browser information can be collected

---

# Localhost

Localhost is the computer itself.

IP Address:

127.0.0.1

When Hound runs in localhost mode:

- Only the same computer can access it.
- Other devices cannot open the page.
- Good for testing.

Example:

http://127.0.0.1:8080

---

# PHP Server

Hound starts a small PHP server.

Example command:

php -S 127.0.0.1:8080

Purpose:

- Hosts the web page locally.
- Sends HTML, CSS, JavaScript to the browser.

---

# Cloudflare Tunnel

Cloudflare Tunnel creates a temporary public URL.

Example:

https://xxxx.trycloudflare.com

Purpose:

- Makes the local PHP server accessible over the Internet.
- Useful for testing from another device that you own.

---

# Browser Information

When the page is opened, Hound can collect:

- Browser Name
- Browser Version
- User Agent
- Language
- Screen Resolution
- CPU Cores
- RAM (if supported)
- Cookies Enabled
- Platform

This information comes from browser APIs.

---

# IP Address

Hound can detect the public IP address.

Example:

157.xxx.xxx.xxx

From the IP address, it may determine:

- Country
- State
- City
- ISP

This is approximate information.

---

# GPS Location

GPS is different from IP location.

GPS requires:

- Browser permission
- Device location enabled

Without permission, GPS location is not available.

---

# Difference Between IP Location and GPS

IP Location

- Approximate
- Based on ISP
- Less accurate

GPS Location

- Requires permission
- Uses device sensors
- Much more accurate

---

# What I Practiced

I tested Hound on:

- My own laptop
- My own Android phone

I learned:

- Localhost only works on the same machine.
- Cloudflare Tunnel provides a temporary public URL.
- Browser asks for location permission.
- GPS is available only after permission is granted.

---

# Important Learning

Information gathering depends on:

- Browser
- Browser permissions
- Network connection
- Device settings

Not every browser provides the same information.

---

# Conclusion

Hound helped me understand browser-based information gathering, local web servers, Cloudflare Tunnel, browser permissions, IP-based location, and GPS location in a controlled lab environment.
