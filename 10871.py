N,X = map(int,input().split())
A = [ str(i) for i in list(map(int,input().split())) if i < X]
print(' '.join(A))