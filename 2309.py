import itertools
height = [int(input()) for _ in range(9)]
answer = ''
for i in itertools.combinations(height,7):
    answer = i
    if sum(i) == 100: break
for i in sorted(answer): print(i)