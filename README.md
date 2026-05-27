# ============ MAC Address Changer ============

## 📌 Description

This project is an educational Python tool designed to automate the process of changing a device's MAC address on Linux systems.

The goal of this project is to better understand:
- How MAC addresses work
- MAC address spoofing concepts
- Network filtering mechanisms
- Basic system automation with Python

⚠️ This project is created strictly for educational and authorized testing purposes only.

---

# 📖 What is a MAC Address?

A **MAC Address (Media Access Control Address)** is a unique physical identifier assigned to a network interface card (NIC).

- It works at **Layer 2 (Data Link Layer)** of the OSI model.
- It is generally written in hexadecimal format:

```bash
XX:XX:XX:XX:XX:XX
```

Example:

```bash
08:00:27:80:69:57
```

A MAC address is composed of:
- The first 3 bytes → identify the manufacturer (**OUI**)
- The last 3 bytes → uniquely identify the device

---

# 🧠 How It Works

The operating system allows temporary modification of the network interface MAC address using system commands.

The process generally consists of:

1. Disabling the network interface
2. Changing the MAC address
3. Re-enabling the interface

---

# ⚙️ Manual Steps to Change a MAC Address

## Step 1 — Check current MAC address

```bash
ifconfig wlan0
```

## Step 2 — Disable interface

```bash
sudo ifconfig wlan0 down
```

## Step 3 — Change MAC address

```bash
sudo ifconfig wlan0 hw ether 00:11:22:33:44:55
```

## Step 4 — Enable interface again

```bash
sudo ifconfig wlan0 up
```

## Step 5 — Verify changes

```bash
ifconfig wlan0
```

---

# 🚀 Project Objective

This project was created to automate the MAC address changing process efficiently using Python.

Educational objectives include:
- Understanding MAC Address Spoofing
- Learning how MAC filtering works
- Understanding network identity concepts
- Practicing Linux networking
- Automating system tasks using Python

Example educational scenarios:
- Testing MAC filtering in a lab
- Privacy and anonymity learning
- Cybersecurity training
- Networking practice

⚠️ This project must only be used in authorized environments.

---

# 🛠️ Technologies & Libraries Used

## Python Libraries

### `subprocess`
Used to execute Linux system commands directly from Python.

Example:

```python
subprocess.call()
```

### `optparse`
Used for command-line argument parsing.

Example:

```python
parser.add_option()
```

### `re`
Used for regular expression matching to validate and extract MAC addresses.

Example:

```python
re.search()
```

---

# 📂 Project Structure

```bash
mac_changer.py
README.md
```
---

# 🚀 Usage

## Run the script

```bash
python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

---

# 📌 Parameters

| Argument | Description |
|----------|-------------|
| `-i` | Network interface |
| `-m` | New MAC address |

---

# 🧠 Example Input

```bash
python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

---

# ✅ Example Output

```bash
[+] Changing MAC Address for wlan0 to 00:11:22:33:44:55
[+] MAC address changed successfully to 00:11:22:33:44:55
```

---

# 🧪 Example Workflow

<img width="1148" height="874" alt="image" src="https://github.com/user-attachments/assets/af4e6dca-4c32-4020-95ec-e983f938b05d" />


---

# 🔐 Ethical Notice

This tool is intended only for:
- Educational purposes
- Authorized security testing
- Personal lab environments

The author is not responsible for any misuse or illegal activity performed using this project.

Always obtain proper authorization before testing on real networks.

---

# 📚 Concepts Covered

- MAC Address
- Network Interfaces
- Linux Networking
- Python Automation
- Regular Expressions
- Ethical Hacking Basics
- Network Privacy
- MAC Filtering

---

# 🏁 Conclusion

This project helped automate the MAC address changing process while providing practical understanding of networking fundamentals and cybersecurity concepts.

It also demonstrates how Python can interact with operating system commands to simplify repetitive networking tasks efficiently.

Future improvements may include:
- MAC vendor randomization
- Interface auto-detection
- GUI version
- Better error handling
- Support for `ip` command instead of `ifconfig`

---

# 👨‍💻 Author

FOUAD NAATANI  
Cybersecurity Engineering Student  
Purple Team & Offensive Security Enthusiast
