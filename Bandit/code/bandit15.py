

# https://overthewire.org/wargames/bandit/bandit16.html

"""
Bandit Level 15 → Level 16
Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

Commands you may need to solve this level
ssh, telnet, nc, openssl, s_client, nmap

Helpful Reading Material
Secure Socket Layer/Transport Layer Security on Wikipedia
OpenSSL Cookbook - Testing with OpenSSL

ssh bandit15@bandit.labs.overthewire.org -p 2220

Password: ?????????????????????????????

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
