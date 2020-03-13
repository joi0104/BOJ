import collections
import sys

def pop_front() :
    num.popleft()
    idx.pop(0)
    for i in range(len(idx)): idx[i] = idx[i] - 1 if idx[i] else len(num) - 1

def move_front():
    num.append(num.popleft())
    for i in range(len(idx)) : idx[i] = idx[i] - 1 if idx[i] else len(num)-1

def move_back():
    num.appendleft(num.pop())
    for i in range(len(idx)): idx[i] = idx[i] + 1 if idx[i] < len(num) - 1 else 0

n , m = map(int,sys.stdin.readline().split())
idx = list(map(lambda x : int(x)-1, sys.stdin.readline().split()))
num = collections.deque([1]*n)
answer = 0
while idx:
    while idx[0] :
        if idx[0] <= len(num)//2 : move_front()
        else : move_back()
        answer += 1
    pop_front()
print(answer)