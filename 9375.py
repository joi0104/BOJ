from functools import reduce
n = int(input())
for _ in range(n):
    d = dict()
    for j in range(int(input())):
        a,b = input().split()
        if b in d.keys() : d[b] += 1
        else : d[b] = 2
    if d : print(reduce(lambda x,y: x*y,d.values())-1)
    else: print(0)
