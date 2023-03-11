

# https://overthewire.org/wargames/bandit/bandit15.html

"""
Bandit Level 14 → Level 15
Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

Commands you may need to solve this level
ssh, telnet, nc, openssl, s_client, nmap

Helpful Reading Material
How the Internet works in 5 minutes (YouTube) (Not completely accurate, but good enough for beginners)
IP Addresses
IP Address on Wikipedia
Localhost on Wikipedia
Ports
Port (computer networking) on Wikipedia


ssh bandit14@bandit.labs.overthewire.org -p 2220

Password: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq


echo fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq | nc localhost 30000


mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

import socket

def send_message(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)
    return data.decode('utf-8').strip()


HOST = 'localhost'
HOST = 'bandit.labs.overthewire.org'
PORT = 30000
MSG = f'fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq\n'

res_msg = send_message(HOST, PORT, MSG)
print (res_msg)


