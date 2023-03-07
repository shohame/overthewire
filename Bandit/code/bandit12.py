

# https://overthewire.org/wargames/bandit/bandit13.html

"""
Bandit Level 12 → Level 13
Level Goal
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

Helpful Reading Material
Hex dump on Wikipedia

ssh bandit12@bandit.labs.overthewire.org -p 2220

Password: JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5

1f8b - is gzip format: .gz

mkdir /tmp/temp
cd /tmp/temp

cat ~/data.txt

    #  1f8b - is gzip format: .gz

xxd -r ~/data.txt data.gz

gzip -d data
xxd -ps data

        Bzip .bz	42 5a	BZ

mv data data.bz
bzip2 -d data
xxd -ps data

        #  gzip format  	.gz	   1f 8b

mv data data.gz
gzip -d data
xxd -ps data
mv data data.tar

tar -xf data.tar
xxd -ps data5.bin

mv data5.bin data5.tar
tar -xf data5.tar

xxd -ps data6.bin

        Bzip	.bz	42 5a

mv data6.bin data6.bz

bzip2 -d data6.bz

xxd -ps data6
mv data6 data6.tar
tar -xf data6.tar

xxd -ps data8.bin
        #  gzip format	.gz	1f 8b
mv data8.bin data8.gz

gzip -d data8

cat data8
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

nano main.py
python3 main.py

rm -r /tmp/temp

"""

from pathlib import Path
path = Path('/')
