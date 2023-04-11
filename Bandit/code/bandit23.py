

# https://overthewire.org/wargames/bandit/bandit24.html

"""

Bandit Level 23 → Level 24
Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler.
Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script.
This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)


ssh bandit23@bandit.labs.overthewire.org -p 2220

Password: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G


cd /etc/cron.d/
cat cronjob_bandit24
cat /usr/bin/cronjob_bandit24.sh

============================================================================================================
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
============================================================================================================

cd /var/spool/bandit24/foo
nano my_script.sh
========================
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/pass24.txt
========================

chmod 777 my_script.sh

Wait 1 minute...

cat /tmp/pass24.txt

do this in level 24!
rm /tmp/pass24.txt

"""


