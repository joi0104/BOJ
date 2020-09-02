n = int(input())
x,y,ans = 0,n+1,0
while x+1 < y:
    a = x+1
    b = n//a if not n%a else n//a+1
    ans += (a*(y-b)+b) if a!=b else a*(y-b)
    x,y = a,b
print(ans)