def make_title(N):
    n = 0
    i = 1
    while True:
        if '666' in str(i) : n += 1
        if n == N : return i
        i += 1

print(make_title(int(input())))

