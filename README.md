# 🔧 MAC Address Changer (Python)

A simple Python script to change the MAC address of a network interface on Linux systems.

---

## ⚙️ Features

* Change MAC address of any network interface
* Verify if the MAC address was successfully changed
* Uses modern `ip` command (more reliable than deprecated tools)
* Lightweight and easy to use

---

## 📦 Requirements

* Python 3
* Linux OS
* Root privileges (`sudo`)
* `ip` and `ifconfig` installed

---

## 🚀 Usage

```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac>
```

### Example:

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

---

## 🧠 How It Works

1. Takes interface and new MAC address as input
2. Brings the interface **down**
3. Changes the MAC address
4. Brings the interface **up**
5. Verifies the change

---

## 📁 Script Overview

* `get_arguments()` → Parses command-line arguments
* `change_mac()` → Applies the MAC address change
* `get_mac_address()` → Retrieves current MAC address
* Main block → Runs the process and verifies success

---

## ⚠️ Disclaimer

This tool is intended **for educational and authorized use only**.

* Do **NOT** use this script on networks or devices you do not own or have explicit permission to test.
* Changing MAC addresses may violate network policies, terms of service, or local laws.
* The author is **not responsible** for any misuse, damage, or legal consequences resulting from the use of this tool.

---

## 🛑 Notes

* Must be run as **root (sudo)**
* Some interfaces may not support MAC address changes
* Network managers (like NetworkManager) may override changes

---

## 📜 License

This project is for educational purposes. You may modify and use it responsibly.

---

## 👨‍💻 Author

SkyKnight25
