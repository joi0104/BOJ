N = int(input())
M = sorted(list(map(int,input().split())))
D = 1000000007
ans = 0
i,j = 0,N-1
a,b = 0,1
while i<j:
    a += (M[j]-M[i])
    b *= (2 if i!=0 else 1)
    b %= D
    ans += ((a*b)%D)
    ans %= D
    i,j = i+1, j-1
if not N%2: i,j = i-1,j+1
while i!=-1:
    a -= (M[j]-M[i])
    b *= (2 if i!=0 else 1)
    b %= D
    ans += ((a*b)%D)
    ans %= D
    i,j = i-1, j+1
print(ans%D)


