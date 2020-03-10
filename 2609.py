from math import gcd
def lcm(n,m):
    return n*m // gcd(n,m)
n,m = map(int,input().split())
print(gcd(n,m))
print(lcm(n,m))