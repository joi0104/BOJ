n = int(input())
time = sorted(sorted([list(map(int,input().split())) for _ in range(n)]),key= lambda x : x[1])
answer = [[0,0]]
for i in time:
    if answer[-1][1] <= i[0] : answer.append(i)
print(len(answer)-1)
