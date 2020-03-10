n = int(input())
p = sorted(list(map(int,input().split())))
time = [0 for i in range(n)]
for i in range(n): time[i] = sum(p[:i+1])
print(sum(time))