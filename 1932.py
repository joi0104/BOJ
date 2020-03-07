dp = [0,0]
for _ in range(int(input())):
    floor = list(map(int, input().split()))
    dp = [0] + [max(dp[j], dp[j+1]) + floor[j] for j in range(len(floor))] + [0]
print(max(dp))