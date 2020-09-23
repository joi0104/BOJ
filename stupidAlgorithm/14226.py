n = int(input())
v = [[0] * 1001 for _ in range(1001)]
v[1][0] = 1
q = [[1, 0]]

for m, c in q:
    if m == n:
        print(v[m][c] - 1)
        break
    for i, j in [[m, m], [m + c, c], [m - 1, c]]:
        if n >= i >= 0 and not v[i][j]:
            v[i][j] = v[m][c] + 1
            q.append([i,j])
