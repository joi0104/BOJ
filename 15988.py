for _ in range(int(input())):
    n = int(input())
    dp = [1,2,4]
    for i in range(3,n): dp[i%3] = (dp[0] + dp[1] + dp[2])%1000000009
    print(dp[(n-1)%3])
