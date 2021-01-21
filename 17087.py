from math import gcd
from functools import reduce
N, S = map(int,input().split())
A = list(map(lambda x: abs(int(x)-S), input().split()))
print(reduce(lambda a,c: gcd(a,c),A,A[0]))