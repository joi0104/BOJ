from collections import Counter
n = int(input())
nums = list(map(int,input().split()))+[-1]
f = Counter(nums)
ngf = [n]*n

for i in range(n-2,-1,-1):
    tmp = i+1
    while tmp != n:
        if f[nums[i]] < f[nums[tmp]]:
            ngf[i] = tmp
            break
        tmp = ngf[tmp]

print(*map(lambda x: nums[x], ngf))
