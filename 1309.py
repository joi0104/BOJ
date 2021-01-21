n = int(input())
dp = [1,1,1]
for _ in range(1,n): dp = [(dp[1]+dp[2])%9901,(dp[0]+dp[2])%9901,(dp[0]+dp[1]+dp[2])%9901]
print(sum(dp)%9901)