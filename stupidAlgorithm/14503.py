def clean(r,c):
    global answer
    room[r][c] = 2
    answer += 1
    return

def move(nr,nc):
    global r,c
    r,c = nr,nc
    return

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
r,c,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]
answer = 0
check_r = [0, -1, 0, 1]
check_c = [-1, 0, 1, 0]

clean(r,c)
while True:
    for i in range(4):
        nr,nc = r + check_r[d],c + check_c[d]
        d = (d + 3) % 4
        if room[nr][nc] == 0:
            move(nr,nc)
            clean(r,c)
            flag = 1
            break;
        else: flag = 0

    if flag == 0:
        nr,nc = r + check_r[(d + 3) % 4],c + check_c[(d + 3) % 4]
        if room[nr][nc] == 1: break
        else: move(nr,nc)

print(answer)