n = int(input())
dp = [0,1,2,3]
for i in range(4,n+1):
    tmp = i
    for j in range(1,i):
        if i-(j**2) < 0: break
        tmp = min(dp[i-(j**2)]+1,tmp)
    dp.append(tmp)
print(dp[n])