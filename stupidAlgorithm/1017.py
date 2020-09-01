def prime(n):
    p = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if p[i]:
            for j in range(2 * i, n+1, i): p[j] = False
    return p

def dfs(i,V):
    V[i] = True
    for j in M[i]:
        if D[j] == -1 or (not V[D[j]] and dfs(D[j],V)):
            D[j] = i
            return 1
    return 0

N=int(input())
X=list(map(int,input().split()))
P=prime(2000)
M=[[j for j in range(N) if P[X[i]+X[j]]] for i in range(N)]
A=[]
for i in range(len(M[0])):
    D = [-1]*N
    if all(dfs(j,[False]*N) for j in range(N)):
        A.append(D.index(0))
        M[0].remove(D.index(0))
print(*sorted([X[i] for i in A]) or -1)