def check(n):
    now = n[0]
    tmp = [now]
    for i in n:
        if now == i : continue
        if i in tmp : return False
        tmp.append(i)
        now = i
    return True

answer = 0

for i in range(int(input())):
    if check(input()): answer += 1
print(answer)