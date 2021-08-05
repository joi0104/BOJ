import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
x = [' ' + y for y in sorted(input().split(), key=lambda z: int(z))]


def dfs(d=0, s=''):
    if d == m:
        print(s[1:]+'\n')
        return
    b = ''
    for j in range(n):
        if b != x[j]:
            b = x[j]
            dfs(d+1, s+x[j])


dfs()