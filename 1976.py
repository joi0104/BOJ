def find(x):
    if x == p[x]:
        return x
    tmp = find(p[x])
    p[x] = tmp
    return tmp


def union(x, y):
    p_x = find(x)
    p_y = find(y)
    if p_x != p_y: p[p_y] = p_x


n, m = int(input()), int(input())
p = [i for i in range(n)]

for x in range(n):
    for y, connect in enumerate(map(int,input().split())):
        if connect: union(x, y)
goal = list(map(lambda x: find(int(x)-1), input().split()))
print('YES' if all(x == goal[0] for x in goal) else 'NO')

