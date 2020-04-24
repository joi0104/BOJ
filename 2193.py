dp = [0,1]
for i in range(1,int(input())): dp = [dp[0]+dp[1],dp[0]]
print(sum(dp))