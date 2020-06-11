import sys
input = sys.stdin.readline
n,m = map(int,input().split())
r,c,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]
answer = 0
check_r, check_c = [0, -1, 0, 1],[-1, 0, 1, 0]

room[r][c],answer = 2, answer+1
while True:
    for i in range(4):
        nr, nc = r + check_r[d], c + check_c[d]
        d = (d + 3) % 4
        if room[nr][nc] == 0:
            r,c = nr, nc
            room[r][c],answer = 2, answer+1
            flag = 1
            break
        else: flag = 0
    if flag == 0:
        nr, nc = r + check_r[(d + 3) % 4], c + check_c[(d + 3) % 4]
        if room[nr][nc] == 1: break
        else: r,c = nr,nc
print(answer)