import functools
def compare_location(a,b):
    print(a,b)
    if a[1] > b[1] : return 1
    if a[1] < b[1] : return -1
    if a[1] == b[1] and a[0] > b[0] : return 1
    if a[1] == b[1] and a[0] < b[0]: return -1
    return 0

N = int(input())
location = [list(map(int,input().split())) for i in range(N)]
for i in sorted(location,key = functools.cmp_to_key(compare_location)) : print(i[0],i[1])
