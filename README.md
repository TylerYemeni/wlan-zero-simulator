# WLAN Zero Simulator

**WLAN Zero Simulator** is a powerful WiFi security auditing tool built for Kali Linux.  
It simulates core features of hardware tools like WLAN 0, combining Python and aircrack-ng to scan, attack, capture, and crack wireless networks.

> **FOR EDUCATIONAL AND AUTHORIZED USE ONLY.**  
> Always ensure you are testing **your own network** or have explicit permission.

---

## Features

- [x] Enable monitor mode on your wireless interface
- [x] Capture WPA/WPA2 handshakes
- [x] Deauthentication attack to force clients to reconnect
- [x] Crack captured handshakes using wordlists
- [x] Clean Python interface for simplified workflow
- [x] Easy to extend with Scapy or other tools

---

## Requirements

- **Python 3**
- **Kali Linux** or any system with:
  - `aircrack-ng`
  - `python3-scapy`
- A WiFi adapter that supports **monitor mode + packet injection**

Install dependencies:
```bash
sudo apt update && sudo apt install aircrack-ng python3-pip
pip3 install -r requirements.txt
