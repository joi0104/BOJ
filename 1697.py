import collections
n, k = map(int,input().split())
q = collections.deque([n])
visit = [-1] * 200001
tmp = q.popleft()
visit[n] = 0
while tmp != k:
    for t in [tmp-1,tmp+1,tmp*2]:
        if 0 <= t <= 200000 and visit[t] == -1:
            q.append(t)
            visit[t] = visit[tmp]+1
    tmp = q.popleft()
print(visit[k])