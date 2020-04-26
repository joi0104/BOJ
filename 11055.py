n = int(input())
nums = list(map(int,input().split()))
dp = [None]*n
answer = 0
for i in range(len(nums)):
    tmp = [nums[i]]
    for j in range(i-1,-1,-1):
        if dp[j][-1] < nums[i] and sum(tmp) <= sum(dp[j]+[nums[i]]): tmp = dp[j] + [nums[i]]
    dp[i] = tmp
    answer = max(answer,sum(dp[i]))
print(answer)
