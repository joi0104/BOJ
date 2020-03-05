import itertools
N,M = map(int,input().split())
tmp = [str(i) for i in range(1,N+1)]
for i in sorted(map(' '.join, itertools.permutations(tmp,M))): print(i)