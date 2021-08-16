def calculate(type, idx, size):
    offset = 1
    result = 0
    for s in range(size, -1, -1):
        tmp = idx + s if type == 'row' else idx + m * s
        visit[tmp] = True
        result += (board[tmp] * offset)
        offset *= 10
    return result

def cleanup(type, idx, size):
    for s in range(size + 1):
        tmp = idx + s if type == 'row' else idx + m * s
        visit[tmp] = False


def is_possible(type, idx, size):
    if type == 'row' and (idx//m) != ((idx+size)//m):
        return False
    if type == 'column' and (idx + m * size) > (n * m - 1):
        return False
    for s in range(size + 1):
        tmp = idx + s if type == 'row' else idx + m * s
        if visit[tmp]: return False
    return True

def dfs(idx, total):
    global answer

    if idx == n*m:
        answer = max(answer, total)
        return

    if visit[idx]:
        dfs(idx+1, total)

    else:
        for size in range(m):
            if is_possible('row', idx, size):
                result = calculate('row', idx, size)
                dfs(idx+1, total + result)
                cleanup('row', idx, size)
        for size in range(n):
            if is_possible('column', idx, size):
                result = calculate('column', idx, size)
                dfs(idx+1, total + result)
                cleanup('column', idx, size)


n, m = map(int, input().split())
board = []
visit = [False] * (m*n)
answer = 0
for _ in range(n):
    board += list(map(int, input()))
dfs(0, 0)
print(answer)

