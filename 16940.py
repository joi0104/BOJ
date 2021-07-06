import sys
import collections
input = sys.stdin.readline
n = int(input())
graph = [[False] * (n+1) for _ in range(n)]

for i in range(n-1):
    x,y = map(int,input().split())
    graph[x][y] = True
    graph[y][x] = True

answer = collections.deque(list(map(int, input().split())))
check = [True, True] + ([False]*(n-1))
queue = collections.deque([answer.popleft()])

while queue:
    q = queue.popleft()
    connect = list(filter(lambda v, i: i if i and(not check[i]) else , graph[q]))
    while connect:
        try:
            a = tmp.popleft()
            connect.remove(a)
            que.append(a)
            check[a] = True
        except:
            print(0)
            exit()
if not que and not tmp and all(check): print(1)
print(0)
