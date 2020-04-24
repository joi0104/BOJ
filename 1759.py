import itertools
l,c = map(int,input().split())
alpa = input().split()
answer = []
for i in itertools.combinations(alpa,l):
    count = 0
    for j in i:
        if j in ['a','e','i','o','u']: count += 1
    if count < 1: continue
    if l-count < 2: continue
    answer.append(''.join(sorted(i)))
for i in sorted(answer): print(i)