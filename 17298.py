n = int(input())
nums = list(map(int,input().split()))
nge_idx = [0]*n

for i in range(n-1,-1,-1):
    if i == n-1: continue
    elif nums[i] < nums[i+1] : nge_idx[i] = i+1
    elif nums[i] == nums[i+1] : nge_idx[i] = nge_idx[i+1]
    else:
        tmp_idx = nge_idx[i+1]
        while nums[tmp_idx] <= nums[i] and tmp_idx: tmp_idx = nge_idx[tmp_idx]
        nge_idx[i] = tmp_idx

for i in range(n): print(nums[nge_idx[i]] if nge_idx[i] else -1, end=' ')