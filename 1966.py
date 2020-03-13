import collections
import sys

for _ in range(int(sys.stdin.readline())):
    n , m = map(int,sys.stdin.readline().split())
    dq = collections.deque(map(int,sys.stdin.readline().split()))
    answer = 0
    while True:
        if dq[0] == max(dq) :
            dq.popleft()
            answer += 1
            if m == 0 :
                print(answer)
                break
            else : m -= 1
        else :
            dq.append(dq.popleft())
            if m == 0: m = len(dq)-1
            else : m -= 1