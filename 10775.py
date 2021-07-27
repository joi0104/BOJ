import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y: parents[root_y] = root_x


g = int(input())
p = int(input())
answer = 0
parents = [i for i in range(g + 1)]

for _ in range(p):
    gi = int(input())
    parents_gi = find(gi)
    if parents_gi == 0: break
    union(parents_gi-1, parents_gi)
    answer += 1

print(answer)
