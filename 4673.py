def d(n):
    sum = n
    for i in str(n) : sum += int(i)
    return sum

tmp = [0 for i in range(10001)]
tmp[0] = 1
for i in range(10001):
    if tmp[i] : continue
    i = d(i)
    while i <= 10000:
        tmp[i] = 1
        i = d(i)

for idx,val in enumerate(tmp) :
    if not val : print(idx)