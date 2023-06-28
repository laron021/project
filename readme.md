![](https://github.com/laron021/project/blob/main/sample/dummy.png)


## Vulnerability scanner and information gathering tool
![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=Python&logoColor=informational&color=blue)
![Kali Linux](https://img.shields.io/static/v1?style=for-the-badge&message=Kali+Linux&color=557C94&logo=Kali+Linux&logoColor=FFFFFF&label=)
![Parrot Linux](https://img.shields.io/badge/Parrot%20Linux-brightgreen?style=for-the-badge&logo=Parrot&logoColor=white#dc143c)
![Docker](https://img.shields.io/badge/-Docker-black?style=for-the-badge&logo=docker)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github)


## NOTES ![Min 3 GB free space needed!](https://img.shields.io/badge/-Min%203%20GB%20free%20space%20needed!-darkred?style=flat-square)
Introducing my project: a vulnerability scanner and information gathering tool designed for beginners! This tool is built to run on Kali,Parrot Linux and is perfect for those who are just starting out in the world of cybersecurity. With this tool, you can quickly and easily scan your system for vulnerabilities and gather information about potential targets.

The tool is designed to be easy to use and requires no prior knowledge of cybersecurity or terminal usage. It features a user-friendly interface and provides step-by-step instructions to guide you through the scanning process. Whether you're looking to secure your own system or want to learn more about cybersecurity, this tool is a great place to start.


# Quick Setup & Run
**Download and Run**
```bash
git clone https://github.com/laron021/project && cd project && sudo python3 dummy_scan.py
```
**Run**
```bash
sudo python3 dummy_scan.py
```
# Guide
![](https://github.com/laron021/project/blob/main/sample/setup%26run.gif)

# Menu
Kali linux & Parrot Linux
![](https://github.com/laron021/project/blob/main/sample/kali2.png)

# Help and info
```
Welcome to help menu
target:                      example.com / 192.168.1.100
target domain:               example.com / trythis.org
target domain with protocol: https://example.com / http://trythis.org

0: Help
1: Check availability
2: DNS enumeration
3: OS detection
4: Service and version detection
5: Vulnerability check with vulners 
6: OWASP ZAP
7: OWASP Nettacker
8: View reports
9: Exit program
10:Remove program
```
1. -TCP SYN ping is useful for discovering alive hosts protected by a stateful firewall.

2. -Uses a perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks. 
    The main purpose of Dnsenum is to gather as much information as possible about a domain.                                                                                                                               
3. -Nmap sends TCP and UDP packets to a particular port, and then analyze its response. It compares this response to a database of 2600 operating systems, and return information on the OS (and version) of a host.

4. -Starts Nmap scan on a given target and probe open ports to determine service/version info.

5. -The vulners script sends CPE descriptions of discovered services by Nmap to the vulners.com vulnerability database API and reports known CVEs in those services.

6. -The OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained  by a dedicated international team of volunteers. It can help you automatically find security vulnerabilities in your web applications while you are developing and testing your applications. It is also a great tool for experienced pentesters to use for manual security testing.                                                                                                                                
7. -OWASP Nettacker project is created to automate information gathering, vulnerability scanning and eventually generating a report for networks, including services,bugs, vulnerabilities, misconfigurations, and other information.

8. -Opens my_reports folder where your scan results are stored. 

9. -Closes the program 

10. -Deletes all components, folders, subfolders, reports, zap docker image and the program itself. 

## License ![Feel free to use](https://img.shields.io/badge/Feel%20free%20to%20use-18A303?style=flat)
This software is licensed under the [MIT](https://github.com/laron021/project/blob/main/LICENSE) License.
