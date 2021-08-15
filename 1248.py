def check(i):
    for j in range(i, -1, -1):
        v = sum(a[j:i+1])
        if s[j][i-j] == '0' and v == 0: continue
        if s[j][i-j] == '+' and v > 0: continue
        if s[j][i-j] == '-' and v < 0: continue
        return False
    return True


def dfs(i):
    if i == n:
        print(*a)
        exit()
    for v in range(-10, 11):
        a[i] = v
        if check(i): dfs(i+1)


n, m = int(input()), input()
s, t = [], 0
a = [0] * n

for i in range(n, 0, -1):
    s.append(m[t:t+i])
    t += i

dfs(0)