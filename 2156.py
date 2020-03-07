n = int(input())
grape = [int(input()) for _ in range(n)]
dp = [grape[0]]
for i in range(1,n):
    if i == 1 : dp.append(max(grape[0],grape[1],grape[0]+grape[1]))
    elif i == 2: dp.append(max(grape[0]+grape[1],grape[1]+grape[2],grape[0]+grape[2]))
    else : dp.append(max(grape[i]+dp[i-2],dp[i-1],grape[i]+grape[i-1]+dp[i-3]))
print(dp[-1])