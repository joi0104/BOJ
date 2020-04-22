import itertools
import math
for _ in range(int(input())):
    n, *nums = map(int,input().split())
    gcd = []
    for i in itertools.combinations(nums,2): gcd.append(math.gcd(i[0],i[1]))
    print(sum(gcd))

