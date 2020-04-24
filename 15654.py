import itertools
n,m = map(int,input().split())
nums = list(map(int,input().split()))
for i in itertools.permutations(sorted(nums),m): print(*i)