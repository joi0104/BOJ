import sys
def f1(a,b):
    if b == 1: return tmp
    if b%2: return (((f1(a,b//2)%c)**2)*(tmp))%c
    return ((f1(a,b//2)%c)**2)%c
a,b,c = map(int,sys.stdin.readline().split())
tmp = a%c
print(f1(a,b))