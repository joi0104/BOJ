n = input()
l = len(n)
answer = 0
for i in range(1, l+1):
    if i == l: answer += (int(n)-(10**(i-1))+1)*i
    else: answer += (9*(10**(i-1))*i)
print(answer)