def check(n):
    n = str(n)
    try: tmp = int(n[0])-int(n[1])
    except: return True
    for i,j in zip(n[:-1],n[1:]):
        if tmp!=(int(i)-int(j)): return False
    return True

n = int(input())
answer = 0
for i in range(1,n+1):
    if check(i) : answer += 1
print(answer)