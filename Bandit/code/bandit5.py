
# https://overthewire.org/wargames/bandit/bandit6.html

"""
Level Goal
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable
1033 bytes in size
not executable
Commands you may need to solve this level
ls , cd , cat , file , du , find

ssh bandit5@bandit.labs.overthewire.org -p 2220

Password: lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

cd /tmp
mkdir perry5
cd /tmp/perry5


 rm -r perry5

find ~/inhere -type f ! -executable -readable -size 1033c -ls

"""

from pathlib import Path

path = Path('/home/bandit5/inhere')
files = list(path.rglob("*"))
files.sort()

for f in files:
    try:
        file1 = open(f, "rb")
        data = file1.read()
        if (len(data) == 1033):
            print (f'{str(f)} :\n {data}')
        file1.close()
    except:
        print(f'{f} : Error reading file!')
