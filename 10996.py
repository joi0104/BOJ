def insert_star_row(row,flag):
        for i in range(2*n):
            if i%2 == flag : t[i][row] = '*'

n = int(input())
t = [[' ' for _ in range(n)] for _ in range(n*2)]
for i in range(n):
    flag = 0
    if i%2 == 1 : flag = 1
    insert_star_row(i,flag)
for i in t : print(''.join(i))