
def print_star(n,tmp,start_row,start_column,option):
    if n == 1 and option:
        tmp[start_row][start_column] = '*'
        return
    elif n == 1 and not option:
        tmp[start_row][start_column] = ' '
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1 : print_star(n//3,tmp,start_row+i*(n//3),start_column+j*(n//3),False)
            elif not option : print_star(n//3,tmp,start_row+i*(n//3),start_column+j*(n//3),False)
            else: print_star(n//3,tmp,start_row+i*(n//3),start_column+j*(n//3),True)

n = int(input())
tmp = [['' for i in range(n)] for i in range(n)]
print_star(n,tmp,0,0,True)
for i in range(n): print(''.join(tmp[i]))
