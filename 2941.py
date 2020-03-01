n = input()
for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    if i in n: n = n.replace(i,'a')
print(len(n))