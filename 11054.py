n = int(input())
num = list(map(int,input().split()))
dp_increase = [0 for _ in range(n)]
dp_decrease = [0 for _ in range(n)]
for i in range(n):
    tmp = []
    for j in range(i):
        if dp_increase[j][-1] < num[i] and len(dp_increase[j]) > len(tmp) :  tmp = dp_increase[j]
    dp_increase[i] = tmp + [num[i]]
for i in range(n-1,-1,-1):
    tmp = []
    for j in range(i+1,n):
        if dp_decrease[j][0] < num[i] and len(dp_decrease[j]) > len(tmp) : tmp = dp_decrease[j]
    dp_decrease[i] = [num[i]] + tmp
for i in range(n):
    tmp = []
    for j in range(i+1,n):
        if dp_decrease[j][0] < dp_increase[i][-1] and len(dp_decrease[j]) > len(tmp) : tmp = dp_decrease[j]
    dp_increase[i] = len(dp_increase[i]+tmp)
print(max(dp_increase))