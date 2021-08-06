import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))
answer = []
for i in range(n-1, 0, -1):
    if a[i] > a[i-1]:
        for j in range(n-1, i-1, -1):
            if a[i-1] < a[j]:
                a[i-1], a[j] = a[j], a[i-1]
                break
        answer = a[:i] + a[n-1:i-1:-1]
        break
print(' '.join(map(str, answer)) if answer else '-1')