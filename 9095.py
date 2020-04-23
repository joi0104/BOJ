def split_n(m,tmp):
    global answer
    if m == 0 :
        answer+=1
        return
    if m >= 3: split_n(m-3,tmp+[3])
    if m >= 2: split_n(m-2,tmp+[2])
    if m >= 1: split_n(m-1,tmp+[1])

for _ in range(int(input())):
    n = int(input())
    answer = 0
    split_n(n,[])
    print(answer)