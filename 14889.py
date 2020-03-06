import sys

def dfs(x,start_num,link_num,start_score,link_score):
    if x == n :
        answer.append(abs(start_score-link_score))
        return
    else:
        for i in range(2):
            team[x] = i
            tmp = 0
            if i == 0:
                if start_num+1 > n//2 : continue
                for j in range(x):
                    if team[j] == team[x] and j != x:
                        tmp += (score[j][x] + score[x][j])
                dfs(x + 1, start_num + 1, link_num, start_score + tmp, link_score)
            else :
                if link_num + 1 > n // 2: continue
                for j in range(x):
                    if team[j] == team[x] and j!=x:
                        tmp += (score[j][x] + score[x][j])
                dfs(x+1,start_num,link_num+1,start_score,link_score+tmp)


n = int(sys.stdin.readline())
score = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
team = [2 for _ in range(n)]
answer = []
dfs(0,0,0,0,0)
print(min(answer))
