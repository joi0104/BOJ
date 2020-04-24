import itertools
while True:
    k, *nums = input().split()
    if not nums: break
    for i in itertools.combinations(nums,6): print(' '.join(i))
    print()
