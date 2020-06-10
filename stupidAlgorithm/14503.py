import sys
input = sys.stdin.readline
n,m = map(int,input().split())
r,c,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]
answer = 0
check_r = [0, -1, 0, 1]
check_c = [-1, 0, 1, 0]

room[r][c],answer = 2, answer+1
while True:
    for i in range(4):
        left_r, left_c = r + check_r[d], c + check_c[d]
        d = (d + 3) % 4
        if room[left_r][left_c] == 0:
            r,c = left_r,left_c
            room[r][c],answer = 2, answer+1
            flag = 1
            break
        else: flag = 0

    if flag == 0:
        back_r, back_c = r + check_r[(d + 3) % 4], c + check_c[(d + 3) % 4]
        if room[back_r][back_c] == 1: break
        else: r,c = back_r,back_c

print(answer)