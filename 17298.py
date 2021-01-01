n = int(input())
nums = list(map(int,input().split()))+[-1]
nge = [n]*n

for i in range(n-2,-1,-1):
    tmp = i+1
    while tmp != n:
        if nums[i] < nums[tmp]:
            nge[i] = tmp
            break
        tmp = nge[tmp]

print(*map(lambda x: nums[x], nge))
