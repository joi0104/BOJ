n = int(input())
x,y,ans = 0,n+1,0
while x+1 < y:
    a = x+1
    b = n//a+(1 if n%a else 0)
    ans += (a*(y-b)+(b if a!=b else 0))
    x,y = a,b
print(ans)