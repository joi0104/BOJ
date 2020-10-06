n = int(input())
q = [(1, 0, 0)]

for m, p, c in q:
    if m == n:
        print(c)
        break
    for i, j, k in [[m, m, c+1], [m + p, p, c+1], [m-1, p, c+1]]:
        if n >= i >= 0: q.append((i, j, k))
