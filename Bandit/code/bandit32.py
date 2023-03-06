

# https://overthewire.org/wargames/bandit/bandit33.html

"""

Bandit Level 32 → Level 33
After all this git stuff its time for another escape. Good luck!

Commands you may need to solve this level
sh, man


ssh bandit32@bandit.labs.overthewire.org -p 2220

Password: ?????????????????????????????

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
