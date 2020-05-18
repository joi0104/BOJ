import heapq
import sys
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    tmp = int(input())
    if tmp: heapq.heappush(heap,(~tmp,tmp))
    else:
        if heap: print(heapq.heappop(heap)[1])
        else: print(0)