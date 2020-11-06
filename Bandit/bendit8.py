


import os
# /home/bandit8/data.txt
with open('data.txt') as f:
    pas = f.read().splitlines()

pas_h = set(pas)
for p in pas_h:
    if pas.count(p) == 1:
        print (p)