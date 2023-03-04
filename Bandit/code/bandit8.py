

# https://overthewire.org/wargames/bandit/bandit9.html

"""
Bandit Level 8 → Level 9
Level Goal
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Helpful Reading Material
Piping and Redirection


ssh bandit8@bandit.labs.overthewire.org -p 2220

Password: TESKZC0XvTetK0S9xNwm25STk5iWrBvP

sort data.txt | uniq -u
-u      Only output lines that are not repeated in the input.


mkdir /tmp/bandit8
cd /tmp/bandit8

nano main.py
python3 main.py

rm -r /tmp/bandit8

"""

from pathlib import Path
import os

if os.name == 'nt':
    fn = Path('../data/bandit8_data.txt')
else:
    fn = Path('/home/bandit8/data.txt')

set_all = set()
set_unique = set()

with open(fn, 'rt') as fid:
    for line in fid:
        line_t = line.strip()
        if line_t not in set_all:
            set_all.add(line_t)
            set_unique.add(line_t)
        else:
            if line_t in set_unique:
                set_unique.remove(line_t)

print(set_unique)


