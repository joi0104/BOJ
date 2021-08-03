def dfs(index , select, length):
    if length == m:
        print(*select)
        return
    if index == n:
        return
    dfs(index + 1, select + [nums[index]], length + 1)
    dfs(index + 1, select, length)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
dfs(0, [], 0)