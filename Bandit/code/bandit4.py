

# https://overthewire.org/wargames/bandit/bandit5.html

"""
Level Goal
The password for the next level is stored in the only human-readable file in the inhere directory.
Tip: if your terminal is messed up, try the “reset” command.

Commands you may need to solve this level
ls , cd , cat , file , du , find

ssh bandit4@bandit.labs.overthewire.org -p 2220

Password: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe







"""


from pathlib import Path
import time
path = Path('/home/bandit4/inhere')
files = path.glob("*")
for f in files:
    file1 = open(f, "r")
    data = file1.read()
    print (f'{f} :\n {data}')
    time.sleep(1)
    file1.close()