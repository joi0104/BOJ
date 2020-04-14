import collections

def backtracking(lucky_string, alpha_dic) :
    global answer
    if len(lucky_string) == n:
        answer += 1
        return
    for i in alpha_dic.keys():
        if not alpha_dic[i] or (lucky_string and i == lucky_string[-1]): continue
        alpha_dic[i] -= 1
        backtracking(lucky_string + i, alpha_dic)
        alpha_dic[i] += 1

string = input()
alpha_dic = collections.Counter(string)
n = len(string)
answer = 0
backtracking('', alpha_dic)
print(answer)