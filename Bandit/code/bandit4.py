

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

