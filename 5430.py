import sys
import collections

for _ in range(int(input())):
    flag_reversed, flag_err = False, False
    p = list(input())
    n = int(input())
    arr = collections.deque(input()[1:-1].split(','))
    if not n : arr = []

    for i in p:
        if i == 'R' : flag_reversed = not flag_reversed
        elif i == 'D' :
            if not arr :
                flag_err = True
                break
            elif flag_reversed : arr.pop()
            else: arr.popleft()

    if flag_err : print('error')
    else :
        arr = list(arr)
        if flag_reversed : arr.reverse()
        print('['+','.join(arr)+']')