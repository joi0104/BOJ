def down(m):
    for i in range(len(m)):
        if i == len(m)-1: break
        if m[i] < m[i+1] : return False
    return True

n = int(input())
m = list(map(int,input().split()))
if m == sorted(m,reverse=True): print(-1)

else:
    idx = 0
    for i in range(len(m)):
        if i == len(m)-1: break
        idx = i
        if down(m[i+1:]) : break
    m[idx], m[-1] = m[-1], m[idx]
    for i in m[:idx+1]+sorted(m[idx+1:]): print(i, end=' ')
