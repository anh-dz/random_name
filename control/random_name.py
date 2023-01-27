import random
f = open("..\\assert\\ds.txt", "r", encoding="utf8")
ls = f.read().split("\n")
f.close()

def ran_name():
    ls_name = []
    for i in range(2):
        select = random.randint(0, len(ls))
        ls_name.append(ls[select])
        ls.pop(select)
    return ls_name

print(ran_name())