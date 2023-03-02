

from pathlib import Path


fn_src = Path('banditXX.py')
with open(fn_src, 'rt') as fid:
    txt_1 = fid.read()
for i in range(16, 35):
    txt = txt_1
    new_txt = txt.replace('%%', str(i+1))
    new_txt = new_txt.replace('!!', str(i))
    fn = f'bandit{i}.py'
    with open(fn, 'wt') as fid:
        txt = fid.write(new_txt)
