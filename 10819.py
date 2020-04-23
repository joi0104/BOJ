def make(x, tmp):
    global answer
    if len(tmp) == n :
        answer = max(answer,calculate(tmp))
        return
    for i in range(len(x)): make(x[:i]+x[i+1:],tmp+[x[i]])

def calculate(y):
    answer = 0
    for i in range(len(y)-1): answer += abs(y[i]-y[i+1])
    return answer

n = int(input())
x = list(map(int,input().split()))
answer = 0
make(x,[])
print(answer)
