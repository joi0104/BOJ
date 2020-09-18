n = int(input())
dp = [[[1 if i==0 and k==1<<j and j!=0 else 0 for k in range(1<<10)] for j in range(10)] for i in range(n)]
for i in range(1,n):
    for j in range(10):
        for k in range(1<<10):
            dp[i][j][k | (1 << j)] += ((0 if j==0 else dp[i - 1][j - 1][k]) + (0 if j==9 else dp[i - 1][j + 1][k])) % 1000000000
print(sum(map(lambda x: dp[n-1][x][(1<<10)-1],range(10))))