def measure():
    if start < 0 and last < 0: return abs(start - last)
    return last - start

import sys
input = sys.stdin.readline
lines = [list(map(int,input().split())) for _ in range(int(input()))]
lines.sort(key = lambda x: x[0])
answer, start, last = 0, lines[0][0], lines[0][1]

for i,j in lines:
    if i <= last <= j: last = j
    if i > last: answer, start, last = answer + measure(), i, j

answer += measure()
print(answer)
