def dfs(i, x, y):
    if i == n+1:
        a.append(x)
        return

    for j in range(len(y)):
        if i == 0: dfs(i+1, x + str(y[j]), y[:j] + y[j + 1:])
        elif l[i - 1] == '<' and int(x[-1]) < y[j]: dfs(i + 1, x + str(y[j]), y[:j] + y[j + 1:])
        elif l[i - 1] == '>' and int(x[-1]) > y[j]: dfs(i + 1, x + str(y[j]), y[:j] + y[j + 1:])


n = int(input())
k = list(range(10))
l = input().split()
a = []
dfs(0, '', k)

print(a[-1])
print(a[0])

