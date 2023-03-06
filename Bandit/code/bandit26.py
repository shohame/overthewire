

# https://overthewire.org/wargames/bandit/bandit27.html

"""

Bandit Level 26 → Level 27
Level Goal
Good job getting a shell! Now hurry and grab the password for bandit27!

Commands you may need to solve this level
ls


ssh bandit26@bandit.labs.overthewire.org -p 2220

Password: ?????????????????????????????

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
