import sys
n =int(sys.stdin.readline())
home = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[[0,0,0]]*n for _ in range(n)]
dp[0][1] = [1,0,0]
for i in range(n):
    for j in range(n):
        if [i, j] == [0, 0] or [i, j] == [0, 1]: continue
        if home[i][j]: dp[i][j] = [0, 0, 0]
        elif i == 0: dp[i][j] = [dp[i][j-1][0],0,0]
        elif j == 0: dp[i][j] = [0,dp[i-1][j][1],0]
        else: dp[i][j] = [dp[i][j-1][0]+dp[i][j-1][2],dp[i-1][j][1]+dp[i-1][j][2],sum(dp[i-1][j-1]) if not home[i-1][j] and not home[i][j-1] else 0]
print(sum(dp[n-1][n-1]))
