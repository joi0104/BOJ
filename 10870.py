def p(n):
    if n == 0 : return 0
    if n == 1: return 1
    return p(n-1) + p(n-2)
print(p(int(input())))