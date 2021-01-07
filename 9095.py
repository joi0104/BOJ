test = [int(input()) for _ in range(int(input()))]
dp = [0,1,2,4]
for i in range(4,max(test)+1): dp.append(dp[i-1]+dp[i-2]+dp[i-3])
for i in test: print(dp[i])