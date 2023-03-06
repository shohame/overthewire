

# https://overthewire.org/wargames/bandit/bandit20.html

"""

Bandit Level 19 → Level 20
Level Goal
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

Helpful Reading Material
setuid on Wikipedia


ssh bandit19@bandit.labs.overthewire.org -p 2220

Password: ?????????????????????????????

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
