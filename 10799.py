answer, laser, line = 0, False, 0
for i in input():
    if i == '(': line, laser = line+1, True
    else: line, answer, laser = line-1, answer + (line-1 if laser else 1), False
print(answer)