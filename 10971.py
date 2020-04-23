def move(current_p, sum, pick_p):
    global answer
    if len(pick_p) == n:
        come_back = route[pick_p[-1]][pick_p[0]]
        if come_back: answer.append(sum+route[pick_p[-1]][pick_p[0]])
        return

    for i in range(n):
        if i not in pick_p and route[current_p][i]:
            move(i,sum+route[current_p][i],pick_p+[i])



n = int(input())
route = [list(map(int,input().split())) for _ in range(n)]
answer = []
for i in range(n): move(i,0,[i])
print(min(answer))