

# https://overthewire.org/wargames/bandit/bandit8.html

"""
Bandit Level 7 → Level 8
Level Goal
The password for the next level is stored in the file data.txt next to the word millionth

Commands you may need to solve this level
man, grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd


ssh bandit7@bandit.labs.overthewire.org -p 2220

Password: z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r temp

cat data.txt | grep -e millionth
grep data.txt -e millionth

try this:
grep millionth data.txt | awk '{print $2}'

"""

from pathlib import Path

fn = Path('/home/bandit7/data.txt')

word_to_find = 'millionth'

with open(fn, 'r') as fid:
    for line in fid:
        if word_to_find in line:
            print (line)
