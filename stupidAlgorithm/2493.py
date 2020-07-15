n = int(input())
top = [100000000] + list(map(int,input().split()))
dp = [0]
for i in range(1,n+1):
    idx = i-1
    while True:
        if top[idx] >= top[i]:
            dp.append(idx)
            break
        idx = dp[idx]
print (*dp[1:])