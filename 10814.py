import functools
def compare_mem(a,b):
    if a[0] > b[0] : return 1
    if a[0] < b[0] : return -1
    if a[0] == b[0] and a[2] < b[2] : return -1
    if a[0] == b[0] and a[2] > b[2]: return 1
    return 0

N = int(input())
mem = []
for i in range(N):
    age , name = input().split()
    mem.append([int(age),name,i+1])
for i in sorted(mem,key= functools.cmp_to_key(compare_mem)): print(i[0],i[1])