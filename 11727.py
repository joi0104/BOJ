n = int(input())
dp = [0,1,3]
for i in range(3,n+1): dp[i%3] = (dp[(i-1)%3]+dp[(i-2)%3]*2)%10007
print(dp[n%3]%10007)