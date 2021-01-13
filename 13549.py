import collections
n, k = map(int,input().split())
queue = collections.deque([n])
time = [-1] * 100101
time[n], tmp = 0, n

while tmp != k:
    i = tmp*2
    while i <= 100100 and time[i] == -1 :
        queue.append(i)
        time[i], i = time[tmp], i*2
    for t in [tmp-1, tmp+1]:
        if 0 <= t <= 100100 and time[t] == -1:
            queue.append(t)
            time[t] = time[tmp]+1
    tmp = queue.popleft()

print(time[tmp])