import random
import os
import shutil

count = 0

if os.stat("..\\assert\\ds_cache.txt").st_size == 0:
    print("Start")
    shutil.copyfile("..\\assert\\ds.txt", "..\\assert\\ds_cache.txt")
f_cache = open("..\\assert\\ds_cache.txt", 'r+', encoding="utf8")

ls = f_cache.read().split(", ")
f_cache.close()

def ran_name():
    try:
        ls_name = []
        for i in range(2):
            select = random.randint(0, len(ls)-1)
            ls_name.append(ls[select])
            ls.pop(select)
        f_cache = open("..\\assert\\ds_cache.txt", 'w', encoding='utf8')
        f_cache.write(', '.join(ls))
        f_cache.close()
        return ls_name
    except:
        return ["DONE", "DONE"]

print(ran_name())
