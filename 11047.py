n, k = map(int,input().split())
coin = reversed([int(input()) for _ in range(n)])
answer = 0
for i in coin:
    if k//i > 0 : answer, k = answer+(k // i) , k-i*(k//i)
print(answer)
