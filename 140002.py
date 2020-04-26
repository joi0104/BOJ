n = int(input())
nums = list(map(int,input().split()))
dp = [None]*n
answer = []
for i in range(len(nums)):
    tmp = [nums[i]]
    for j in range(i-1,-1,-1):
        if dp[j][-1] < nums[i] and len(tmp) <= len(dp[j]): tmp = dp[j] + [nums[i]]
    dp[i] = tmp
    if len(answer) < len(dp[i]): answer = dp[i]
print(len(answer))
print(*answer)
