n = int(input())
dp = [1]*10
for i in range(1,n):
    for j in range(9,-1,-1):
        dp[j] = sum(dp[:j+1])%10007
print(sum(dp)%10007)