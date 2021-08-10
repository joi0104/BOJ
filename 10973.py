import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))
p = -1

for i in range(n-1, 0, -1):
    if a[i] < a[i-1]:
        p = i
        break

for i in range(n-1, p - 1, -1):
    if p != -1 and a[i] < a[p - 1]:
        a[i], a[p - 1] = a[p - 1], a[i]
        break

print(' '.join(map(str, a[:p] + a[n - 1:p - 1:-1])) if p != -1 else '-1')