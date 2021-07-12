def dfs(i, visit):
    if len(visit) == 5:
        print(1)
        exit()
    for j in c[i]:
        if j not in visit:
            dfs(j, visit+[j])


n, m = map(int, input().split())
c = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    c[a].append(b)
    c[b].append(a)

for i in range(n): dfs(i, [i])
print(0)