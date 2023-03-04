

# https://overthewire.org/wargames/bandit/bandit10.html

"""
Bandit Level 9 → Level 10
Level Goal
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd


ssh bandit9@bandit.labs.overthewire.org -p 2220

Password: EN632PlfYiZbn3PhVK3XOGSlNInNE00t

strings data.txt

strings data.txt | grep -E "===+"

https://www.asciitable.com/

mkdir /tmp/bandit9
cd /tmp/bandit9

nano main.py
python3 main.py

rm -r /tmp/bandit9

"""

from pathlib import Path
import os

char_to_find = b'==='

if os.name == 'nt':
    fn = Path('../data/bandit9_data.txt')
else:
    fn = Path('/home/bandit9/data.txt')

with open(fn, 'rb') as fid:
    bin = fid.read()

i = bin.find(char_to_find)
while (i != -1):
    for j, byte in enumerate(bin[i:]):
        if byte < 32 or byte > 128:
            break

    print (bin[i:i+j])
    i = bin.find(char_to_find, i+j)

