

# https://overthewire.org/wargames/bandit/bandit12.html

"""
Bandit Level 11 → Level 12
Level Goal
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Helpful Reading Material
Rot13 on Wikipedia

https://en.wikipedia.org/wiki/ROT13

ssh bandit11@bandit.labs.overthewire.org -p 2220

Password: 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM


cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""
import os
from pathlib import Path

if os.name == 'nt':
    fn = Path('../data/bandit11_data.txt')
else:
    fn = Path('/home/bandit11/data.txt')

with open(fn, 'r') as fid:
    txt = fid.read()

import string

def rotate(ch : str, text : str, cnt : int) -> str:
    assert ch in text, f'{ch} are not in {text}'
    i = text.find(ch)
    i_ = (i + cnt) % len(text)
    return text[i_]

a2z = string.ascii_lowercase
A2Z = string.ascii_uppercase

text = ''
for c in txt:
    if c in a2z:
        text += rotate(c, a2z, 13)
    elif c in A2Z:
        text += rotate(c, A2Z, 13)
    else:
        text += c
print(text)
