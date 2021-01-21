n = int(input())
m = list(map(int,input().split()))
answer, dp = 0, [0, 0]

for i in range(n):
    dp = [max(dp[0] + m[i], m[i]), max(dp[0], dp[1]+m[i])]
    answer = max(dp[0], dp[1], answer)

if answer == 0 and 0 not in m: answer = max(m)
print(answer)
