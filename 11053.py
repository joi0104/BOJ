n = int(input())
num = list(map(int,input().split()))
dp = []
for i in range(n):
    tmp = 0
    for j in range(i):
        if num[j] < num[i] and dp[j] > tmp :  tmp = dp[j]
    dp.append(tmp+1)
print(max(dp))