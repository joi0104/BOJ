n,m = map(int,input().split())
need = [[] for _ in range(n)]
match = [-1 for _ in range(n)]
ans = 0
for i in range(m):
    a,b = map(int,input().split())
    need[a-1].append(b-1)

def solve(i):
    if visited[i]:
        return 0
    visited[i] = True
    for n in need[i]:
        if match[n] == -1 or solve(match[n]):
            match[n] = i
            return 1

for i in range(n):
    visited = [False]*n
    if solve(i): ans+=1
print(ans)