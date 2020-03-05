def solve(tmp):
    global answer

    if len(tmp) == M:
        answer.append(tmp)
        return
    else:
        for i in range(N):
           if not tmp or int(tmp[-1]) <= i+1 :
               solve(tmp+[str(i+1)])
        return

N,M = map(int,input().split())
answer = []
solve([])
for i in answer : print(' '.join(i))