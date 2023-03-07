

# https://overthewire.org/wargames/bandit/bandit11.html

"""
Bandit Level 10 → Level 11
Level Goal
The password for the next level is stored in the file data.txt, which contains base64 encoded data

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Helpful Reading Material
Base64 on Wikipedia


ssh bandit10@bandit.labs.overthewire.org -p 2220

Password: G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp


base64 -d data.txt

"""

import os
import base64
from pathlib import Path

if os.name == 'nt':
    fn = Path('../data/bandit10_data.txt')
else:
    fn = Path('/home/bandit10/data.txt')

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


with open(fn, 'r') as fid:
    b64 = fid.read()

txt = base64ToString(b64)
print(txt)

