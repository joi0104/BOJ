import collections
from queue import PriorityQueue
M, N = map(int,input().split())
MAX = N+M
MAP = [input() for _ in range(N)]
VISIT = [[MAX]*M for _ in range(N)]
VISIT[0][0] = 0
QUEUE = PriorityQueue()
n, m = [0, 0]
while [n, m] != [N-1,M-1]:
    for i, j in [[n-1, m], [n, m+1], [n+1, m], [n, m-1]]:
        if 0 <= i < N and 0 <= j < M and VISIT[i][j] > (VISIT[n][m] + (1 if MAP[i][j] == '1' else 0)):
            VISIT[i][j] = VISIT[n][m] + (1 if MAP[i][j] == '1' else 0)
            QUEUE.put((VISIT[i][j], [i, j]))
    n, m = QUEUE.get()[1]
print(VISIT[N-1][M-1])



