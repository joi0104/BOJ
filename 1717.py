import sys


def find(x):
    if p[x] == x:
        return x;
    tmp = find(p[x])
    p[x] = tmp
    return tmp


def union(x, y):
    p_x = find(x)
    p_y = find(y)
    if p_x != p_y: p[p_y] = p_x


n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a:
        print('YES' if find(b) == find(c) else 'NO')
    else:
        union(b, c)
