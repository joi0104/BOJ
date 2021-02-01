n, m = int(input()), int(input())
init = 100
button = set(map(int, input().split())) if m else set()
answer = abs(n - init)
tmp = init
while ((tmp - n) if n > init else (n - tmp)) < answer and tmp > 0:
    tmp += (1 if n > init else -1)
    if any(map(lambda t: int(t) in button, str(tmp))): continue
    answer = min(answer, abs(tmp - n) + len(str(tmp)))
print(answer)
