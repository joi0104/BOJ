import sys

def check_row(row,value):
    if value in board[row]: return False
    return True

def check_column(column,value):
    for i in range(9):
        if value == board[i][column] : return False
    return True

def check_box(row,column,value):
    idx = [row // 3 * 3, column // 3 * 3]
    for i in range(3):
        for j in range(3):
            if value == board[idx[0] + i][idx[1] + j]:
                return False
    return True

def dfs(x):
    if x == len(zero):
        for i in range(9):
            for j in range(9):
                print(board[i][j],end=' ')
            print()
        sys.exit(0)
    else:
        for j in range(1,10):
            if check_row(zero[x][0],j) and check_column(zero[x][1],j) and check_box(zero[x][0],zero[x][1],j):
                board[zero[x][0]][zero[x][1]] = j
                dfs(x+1)
                board[zero[x][0]][zero[x][1]] = 0

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
dfs(0)