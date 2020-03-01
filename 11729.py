def hanoi(n,one,two,three,answer):
    if n == 1:
        answer.append([one,three])
        return
    hanoi(n-1,one,three,two,answer)
    hanoi(1,one,two,three,answer)
    hanoi(n-1,two,one,three,answer)

answer = []
hanoi(int(input()),1,2,3,answer)
print(len(answer))
for i in answer: print(i[0],i[1])