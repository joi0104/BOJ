n,k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
for x in range(n+1):
    for y in range(k+1):
        if y == 1:
            dp[x][y] = 1
            continue
        for z in range(0,x+1):
            dp[x][y] += dp[x-z][y-1]
            dp[x][y] %= 1000000000
print(dp[n][k])
