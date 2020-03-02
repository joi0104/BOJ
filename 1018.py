def counting(board,i,j):
    W,B = 'W','B'
    count1 = 0
    count2 = 0
    for n in range(8):
        for m in range(8):
            if board[i+m][j+n] == W : count1 += 1
            if board[i+m][j+n] == B : count2 += 1
            W,B = B,W
        W, B = B, W
    return min(count1,count2)

N,M = map(int,input().split())
board = [input() for i in range(N)]
answer = 64
for i in range(N-7):
    for j in range(M-7):
        tmp = counting(board,i,j)
        if answer > tmp : answer = tmp
print(answer)