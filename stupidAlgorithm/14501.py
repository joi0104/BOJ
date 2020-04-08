def backtracking(schedule, i, sum):
    if i == n :
        answer.append(sum)
        return
    if True not in schedule[i:i+chart[i][0]] and i + chart[i][0] <= n:
        backtracking(schedule[:i]+ ([True]*chart[i][0]) + schedule[i+chart[i][0]:], i+1, sum + chart[i][1])
    backtracking(schedule, i+1, sum)


n = int(input())
chart = [list(map(int,input().split())) for _ in range(n)]
answer = []
backtracking([False]*n, 0, 0)
print(max(answer))
