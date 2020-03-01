import string
tmp = {i:'-1' for i in string.ascii_lowercase}
for idx, val in enumerate(input()):
    if tmp[val] != '-1' : continue
    tmp[val] = str(idx)
print(' '.join(tmp.values()))