

# https://overthewire.org/wargames/bandit/bandit22.html

"""

Bandit Level 21 → Level 22
Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler.
Look in /etc/cron.d/ for the configuration and see what command is being executed.

Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)


ssh bandit21@bandit.labs.overthewire.org -p 2220

Password: NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

cd /etc/cron.d
cat cronjob_bandit22

cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv



mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
