import itertools

def check(n):
    n = n.split()
    for i in range(len(n)):
        try:
            if n[i] > n[i + 1]: return False
        except:
            return True

N, M = map(int, input().split())
tmp = [str(i) for i in range(1, N + 1)]
for i in sorted(map(' '.join, itertools.permutations(tmp, M))):
    if check(i): print(i)
