n = int(input())
answer = ''
while n:
    a, b = divmod(n, -2)
    if b == -1: a, b = a+1, -b
    answer = str(b) + answer
    n = a
print(answer or 0)