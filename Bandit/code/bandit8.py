

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

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
