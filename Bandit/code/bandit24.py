

# https://overthewire.org/wargames/bandit/bandit25.html

"""

Bandit Level 24 → Level 25
Level Goal
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24
and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the
10000 combinations, called brute-forcing.
You do not need to create new connections each time


ssh bandit24@bandit.labs.overthewire.org -p 2220

Password: VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

delete the file from the bandit23:
rm /tmp/pass24.txt






mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
