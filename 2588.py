N,M = int(input()),input()[::-1]
answer = 0
for i in range(3):
    temp = N*int(M[i])
    print(temp)
    answer += temp*10**i
print(answer)
