

# https://overthewire.org/wargames/bandit/bandit7.html

"""
Bandit Level 6 → Level 7
Level Goal
The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size
Commands you may need to solve this level
ls , cd , cat , file , du , find , grep

ssh banditll6@bandit.labs.overthewire.org -p 2220

Password: P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

find / -type f -user bandit7 -group bandit6 -size 33c -ls 2>dev/null

"""

from pathlib import Path

path = Path('/')
files = path.rglob("*")

for f in files:
    try:
        if f.stat().st_size == 33 and f.owner() == 'bandit7' and f.group() == 'bandit6':
            print (f'{f} - owner = {f.owner()} - group = {f.group()}')
            with open(f, 'r') as fid:
                print (f'Password: {fid.read()}')

    except:
        pass
        # print(f'{f} : Error ...!')


