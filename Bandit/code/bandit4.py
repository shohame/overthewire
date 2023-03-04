

# https://overthewire.org/wargames/bandit/bandit5.html

"""
Level Goal
The password for the next level is stored in the only human-readable file in the inhere directory.
Tip: if your terminal is messed up, try the “reset” command.

Commands you may need to solve this level
ls , cd , cat , file , du , find

ssh bandit4@bandit.labs.overthewire.org -p 2220

Password: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

cd /tmp
mkdir perry4
git cd perry4
cd /tmp/perry4


rm -r /tmp/perry4

whoami
getent passwd
getent group
getent passwd bandit4
getent group bandit4

ll
ll /etc

drwxr-xr-x   2 root     root       4096 Feb 16 02:10 libnl-3/
drwxr-xr-x   4 root     root       4096 Feb 21 21:58 lighttpd/
-rw-r--r--   1 root     root       2996 Mar  4  2022 locale.alias
-rw-r--r--   1 root     root       9456 Feb 16 02:11 locale.gen
lrwxrwxrwx   1 root     root         27 Feb 16 02:10 localtime -> /usr/share/zoneinfo/Etc/UTC
drwxr-xr-x   4 root     root       4096 Feb 16 02:10 logcheck/


"""


from pathlib import Path

path = Path('/home/bandit4/inhere')
files = path.glob("*")
files.sort()

for f in files:
    try:
        file1 = open(f, "rb")
        data = file1.read()
        print (f'{f} :\n {data}')
        file1.close()
    except:
        print(f'{f} :\n Error reading file!')

