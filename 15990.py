c = 1000000009
for _ in range(int(input())):
    n = int(input())
    dp = [[1,0,0],[0,1,0],[1,1,1]]
    for i in range(3,n):
        dp[i%3] = [(dp[(i-1)%3][1]+dp[(i-1)%3][2])%c,
                   (dp[(i-2)%3][0]+dp[(i-2)%3][2])%c,
                   (dp[(i-3)%3][0]+dp[(i-3)%3][1])%c]
    print(sum(dp[(n-1)%3])%c)