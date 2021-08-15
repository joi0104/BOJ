import sys
input = sys.stdin.readline
print = sys.stdout.write


def mutiply (a, b):
    answer = 0
    for i in range(len(a)): answer += (a[i]*b[i])
    return answer



n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]
c = []

for i in range(k):
    tmp = []
    for j in range(m):
        tmp.append(b[j][i])
    c.append(tmp)

for i in range(n):
    for j in range(k):
        print(str(mutiply(a[i], c[j]))+' ')
    print('\n')
