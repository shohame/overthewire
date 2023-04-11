

# https://overthewire.org/wargames/bandit/bandit21.html

"""

Bandit Level 20 → Level 21
Level Goal
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port
you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password
in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

Commands you may need to solve this level
ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)

and:

&, fg, bg, jobs, top ...


ssh bandit20@bandit.labs.overthewire.org -p 2220

Password: VxCazJaVykI6W36BkBU0mJTCM8rR95XT


# in one terminal:
nc -l 2222 < /etc/bandit_pass/bandit20

# in the second terminal:
./suconnect 2222

or using &: nc -l 2222 < /etc/bandit_pass/bandit20& ...




mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py server&

python3 main.py client

rm -r /tmp/temp

"""

from pathlib import Path

import sys
import subprocess
import socket


def TCP_Server(port):
    path = Path('/')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))

    server_socket.listen(1)

    print(f"Listening on localhost: {port}...")

    client_socket, address = server_socket.accept()
    print(f"Connection from {address} established!")

    message = "VxCazJaVykI6W36BkBU0mJTCM8rR95XT"

    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print(f"Received message from client: {data.decode()}")

    client_socket.close()

def TCP_run_client(port):
    result = subprocess.run(['/home/bandit20/suconnect', f'{port}'], stdout=subprocess.PIPE)

if __name__=="__main__":
    port = 2222
    arg1 = sys.argv[1]

    if arg1=='server':
        print('Running server...')
        TCP_Server(port=port)

    if arg1 == 'client':
        print ('Running client...')
        TCP_run_client(port=port)




