n = int(input())
t = [int(input()) for i in range(n)]
dp = []
for i in range(n):
    if i == 0 : dp.append(t[0])
    elif i == 1 : dp.append(max(dp[0]+t[1],t[1]))
    elif i == 2 : dp.append(max(dp[0]+t[2],t[1]+t[2]))
    else : dp.append(max(dp[i-2],dp[i-3]+t[i-1])+t[i])
print(dp[-1])