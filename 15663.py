import sys
input = sys.stdin.readline
print = sys.stdout.write


n, m = map(int, input().split())
x = input().split()
x.sort(key = lambda x: int(x))
v = [False] * n
s = [None] * m


def dfs(d=0):
    if d == m:
        print(" ".join(s)+"\n")
        return
    else:
        b = ''
        for i in range(n):
            if (not v[i]) & (b != x[i]):
                v[i] = True
                s[d] = x[i]
                b = x[i]
                dfs(d + 1)
                v[i] = False


dfs()