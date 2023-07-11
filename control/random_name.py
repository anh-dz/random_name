import random, os

def group_ls(N, ls):
    return [ls[n:n+N] for n in range(0, len(ls), N)]

c = -1
c_odd = False
with open('assert/ds.txt', 'r', encoding='utf-8') as f:
    ls = f.read().split('\n')
    if len(ls)&1:
        ls.pop(0)
        c_odd = True
    random.shuffle(ls)
    gr_ls = group_ls(2, ls)

with open('assert/ds_cd.txt', 'r', encoding='utf-8') as f:
    ls_cd = f.read().split('\n')
    ls_cd = [i.split('-') for i in ls_cd]
    random.shuffle(ls_cd)

ls_all = gr_ls+ls_cd
if c_odd:
    ls_all.insert(0, ['NHẬT ANH', 'VŨ QUANG DUY'])
# print(ls_all)

def ran_name():
    global c
    c+=1
    if c<len(ls_all):
        return ls_all[c]
    else:
        if os.name=='posix':
            os.system(f'open {os.path.dirname(os.path.abspath(__file__))}/cat.jpg')
        else:
            os.system(f'start {os.path.dirname(os.path.abspath(__file__))}/cat.jpg')
        return ['HAPPY', 'NEW YEAR']