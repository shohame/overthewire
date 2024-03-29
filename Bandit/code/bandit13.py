

# https://overthewire.org/wargames/bandit/bandit14.html

"""
Bandit Level 13 → Level 14
Level Goal
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

Commands you may need to solve this level
ssh, telnet, nc, openssl, s_client, nmap

Helpful Reading Material
SSH/OpenSSH/Keys

ssh bandit13@bandit.labs.overthewire.org -p 2220

Password: wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw


ssh bandit14@localhost -p2220 -i sshkey.private

cat /etc/bandit_pass/bandit14

"""

from pathlib import Path
path = Path('/')
