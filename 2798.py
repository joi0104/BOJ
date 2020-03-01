N,M = map(int,input().split())
card = sorted(map(int,input().split()),reverse=True)
answer = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            tmp = card[i]+card[j]+card[k]
            if tmp <= M and abs(M-answer) >= abs(M-tmp) :
                answer = tmp

print(answer)