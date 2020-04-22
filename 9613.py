import itertools
import math
for _ in range(int(input())):
    n, *nums = map(int,input().split())
    print(sum([math.gcd(i[0],i[1]) for i in itertools.combinations(nums,2)]))

