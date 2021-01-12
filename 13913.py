import collections
n,k = map(int,input().split())
queue = collections.deque([n])
visit = [-2] * 100101
visit[n], tmp, answer = -1, -2, []

while tmp != k:
    for t in [tmp-1, tmp+1, tmp*2]:
        if t>=0 and t<=1001000 and visit[t] == -2:
            queue.append(t)
            visit[t] = tmp
    tmp = queue.popleft()

while tmp != -1:
    answer.append(tmp)
    tmp = visit[tmp]

print(len(answer)-1)
print(*reversed(answer))
