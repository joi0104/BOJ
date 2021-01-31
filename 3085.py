def count():
    b_r = board
    b_c = list(map(lambda x: list(x), zip(*b_r)))
    a = 0
    tmp = 1
    for i in[b_r,b_c]:
        for j in i:
            for k in range(1,len(j)):
                if j[k] == j[k-1]:
                    tmp += 1
                else:
                    a = max(a,tmp)
                    tmp = 1
            a = max(a, tmp)
            tmp = 1
    return a

n = int(input())
board = [list(input()) for _ in range(n)]
answer = 1
for i in range(n):
        for j in range(n):
            if j < (n-1):
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                answer = max(answer, count())
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            if i < (n-1):
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                answer = max(answer, count())
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(answer)