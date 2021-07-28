import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    p_x = parents[x]
    p_y = parents[y]
    if p_x != p_y:
        if p_y > p_x: parents[p_y] = p_x
        else: parents[p_x] = p_y


def is_overlap(i, j):
    x = i[0] - j[0]
    y = i[1] - j[1]
    z = i[2] + j[2]
    return (x * x + y * y) <= (z * z)


t = int(input())
for _ in range(t):
    n = int(input())
    towers = [list(map(int, input().split())) for _ in range(n)]
    parents = [i for i in range(n)]
    for i in range(n):
        for j in range(i):
            if find(i) != find(j) and is_overlap(towers[i], towers[j]):
                union(i, j)
    for i in range(n): find(i)
    print(len(set(parents)))

