n = int(input())
t = sorted([int(input()) for _ in range(n)])
m = []
for i in range(2,t[0]):
    m.append(i)
    for j in range(1,len(t)):
        if t[j-1]%i != t[j]%i :
            m.pop(-1)
            break
            
print(*m)