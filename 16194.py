n = int(input())
pack = list(map(int,input().split()))
dp = []
for i in range(n):
    tmp = pack[i]
    for j in range(i): tmp = min(dp[j]+pack[i-1-j],tmp)
    dp.append(tmp)
print(dp[-1])