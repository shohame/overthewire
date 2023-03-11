

# https://overthewire.org/wargames/bandit/bandit17.html

"""
Bandit Level 16 → Level 17
Level Goal
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Commands you may need to solve this level
ssh, telnet, nc, openssl, s_client, nmap

Helpful Reading Material
Port scanner on Wikipedia

ssh bandit16@bandit.labs.overthewire.org -p 2220

Password: JQttfApK4SeyHwDlI9SXGR50qclOAil1


nmap -p31000-32000 localhost

31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown


echo "JQttfApK4SeyHwDlI9SXGR50qclOAil1" | openssl s_client -connect localhost:31046 -ign_eof
echo "JQttfApK4SeyHwDlI9SXGR50qclOAil1" | openssl s_client -connect localhost:31518 -ign_eof
echo "JQttfApK4SeyHwDlI9SXGR50qclOAil1" | openssl s_client -connect localhost:31691 -ign_eof
echo "JQttfApK4SeyHwDlI9SXGR50qclOAil1" | openssl s_client -connect localhost:31790 -ign_eof
echo "JQttfApK4SeyHwDlI9SXGR50qclOAil1" | openssl s_client -connect localhost:31960 -ign_eof

echo JQttfApK4SeyHwDlI9SXGR50qclOAil1 | nc localhost 31046
echo JQttfApK4SeyHwDlI9SXGR50qclOAil1 | nc localhost 31518
echo JQttfApK4SeyHwDlI9SXGR50qclOAil1 | nc localhost 31691
echo JQttfApK4SeyHwDlI9SXGR50qclOAil1 | nc localhost 31790
echo JQttfApK4SeyHwDlI9SXGR50qclOAil1 | nc localhost 31960




mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

import socket

def port_scan(address, port_range):
    open_ports = []
    for port in range(*port_range):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1) # Set a timeout for the connection attempt
            result = s.connect_ex((address, port))
            if result == 0:
                open_ports.append(port)
    return open_ports


import socket

def send_message(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        try:
            data = s.recv(1024)
        except:
            print(f'Port: {port} not responded.')
            return ''
    return data.decode('utf-8').strip()


address = 'localhost'
port_range = (31000, 32001)
ports_list = port_scan(address, port_range)
print ('open ports: ', ports_list)

HOST = 'localhost'
MSG = f'JQttfApK4SeyHwDlI9SXGR50qclOAil1\n'
for port in ports_list:
    res_msg = send_message(HOST, port, MSG)
    if len(res_msg)>0:
        print (f'Port {port}: ', res_msg)


