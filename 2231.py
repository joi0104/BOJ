def find_constructor(n):
    answer = []
    for i in range(n):
        if sum(map(int,str(i)))+i == n : return i
    return 0
print(find_constructor(int(input())))