

# https://overthewire.org/wargames/bandit/bandit26.html

"""

Bandit Level 25 → Level 26
Level Goal
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

Commands you may need to solve this level
ssh, cat, more, vi, ls, id, pwd


ssh bandit25@bandit.labs.overthewire.org -p 2220

Password: ?????????????????????????????

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
