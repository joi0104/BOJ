import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    sticker = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    dp = [0,0,0]
    for i in range(n): dp = [max(dp[1],dp[2]) + sticker[0][i],max(dp[0],dp[2]) + sticker[1][i],max(dp)]
    print(max(dp))