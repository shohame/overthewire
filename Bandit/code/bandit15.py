

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

Password: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt


echo "jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt" | openssl s_client -connect localhost:30001 -ign_eof



mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""


""" it doesn't work.

import socket 
import ssl

def send_ssl_message(server_hostname, port, message):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Wrap the socket with an SSL context
    context = ssl.create_default_context()
    ssl_sock = context.wrap_socket(s, server_hostname="localhost")
    # Connect to the server
    ssl_sock.connect((server_hostname, port))
    # Send the message
    ssl_sock.sendall(message)
    # Receive the response
    response = ssl_sock.recv(1024)
    # Close the socket
    ssl_sock.close()
    return response.decode()


server_hostname = 'localhost'
port = 300001
message = f'jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt\n'
response = send_ssl_message(server_hostname, port, message)

print (response)

"""

