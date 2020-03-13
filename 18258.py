import collections
import sys
dq = collections.deque()
for _ in range(int(sys.stdin.readline())):
    c = sys.stdin.readline().split()
    if c[0] == 'push' :
        dq.append(c[1])
    elif c[0] == 'pop' :
        if dq : print(dq.popleft())
        else: print(-1)
    elif c[0] == 'size' :
        print(len(dq))
    elif c[0] == 'empty' :
        if dq : print(0)
        else: print(1)
    elif c[0] == 'front' :
        if dq : print(dq[0])
        else: print(-1)
    elif c[0] == 'back' :
        if dq : print(dq[-1])
        else: print(-1)
