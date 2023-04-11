

# https://overthewire.org/wargames/bandit/bandit23.html

"""

Bandit Level 22 → Level 23
Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler.
Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill.
The script for this level is intentionally made easy to read. If you are having problems understanding what it does,
try executing it to see the debug information it prints.

Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)


ssh bandit22@bandit.labs.overthewire.org -p 2220

Password: WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff


cd /etc/cron.d/
cat cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
============================================================================================================
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
cat /tmp/$mytarget

============================================================================================================

myname="bandit23"
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

mkdir /tmp/temp
cd /tmp/temp

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
