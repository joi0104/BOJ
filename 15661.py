import sys
input = sys.stdin.readline

def dfs(i, s1_member, s1_score, s2_member, s2_score):
    if i == n:
        a.append(abs(s1_score-s2_score))
        return

    s1_new_score = s1_score + sum([S[i][j] + S[j][i] for j in s1_member])
    s1_member.append(i)
    dfs(i+1, s1_member, s1_new_score, s2_member, s2_score)
    s1_member.pop()

    s2_new_core = s2_score + sum([S[i][j] + S[j][i] for j in s2_member])
    s2_member.append(i)
    dfs(i+1, s1_member, s1_score, s2_member, s2_new_core)
    s2_member.pop()


n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]
a = []
dfs(0, [], 0, [], 0)
print(min(a))

