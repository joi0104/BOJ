import sys

r, c = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline() for _ in range(r)]
answer = 0


def dfs(x, y, count, check):
    global answer

    for i, j in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
        if 0 <= i < r and 0 <= j < c and not check & (1 << ord(board[i][j]) - 65):
            dfs(i, j, count + 1, check | (1 << ord(board[i][j]) - 65))

    answer = max(answer, count)
    return


dfs(0, 0, 1, (1 << ord(board[0][0]) - 65))
print(answer)