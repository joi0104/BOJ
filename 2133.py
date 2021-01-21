n = int(input())
dp = [0]*(n+1)
dp[0] = 1
if n%2: print(0)
else:
    for i in range(2,n+1):
        for j in range(i-2,-1,-2):
            if j == i-2: dp[i] += (dp[j]*3)
            else: dp[i] += (dp[j]*2)
    print(dp[n])
