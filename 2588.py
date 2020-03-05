N,M = int(input()),list(map(int,list(input())))
for i in range(3):
    M[2-i] = N*M[2-i]
    print(M[2-i])
print(M[0]*100+M[1]*10+M[2])
