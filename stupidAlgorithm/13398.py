n = int(input())
m = list(map(int,input().split()))
s = b = -1e9

for i in range(n):
    if s-r < 0: s,r = m[i],0
    else: s,r = s+m[i], min(r,m[i])
    b = max(s-r, b)

print(b)