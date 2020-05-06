n = int(input())
answer = [1,3]
for i in range(2,n): answer.append(answer[-1] + (answer[-2]*2))
print(answer[n-1]%10007)