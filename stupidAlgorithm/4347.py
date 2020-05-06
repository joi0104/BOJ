import sys
check_line = [[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]
for _ in range(int(sys.stdin.readline())):
    count_x ,count_o,fill_x,fill_o = 0,0,0,0
    grid = []
    for _ in range(3):
        tmp = sys.stdin.readline()[:-1]
        grid.append(tmp)
        count_x, count_o = count_x + tmp.count('X'), count_o + tmp.count('O')
        if tmp == 'XXX': fill_x += 1
        elif tmp == 'OOO': fill_o += 1
    for i,j,z in check_line:
        if grid[i[0]][i[1]]+grid[j[0]][j[1]]+grid[z[0]][z[1]] == 'XXX': fill_x += 1
        elif grid[i[0]][i[1]]+grid[j[0]][j[1]]+grid[z[0]][z[1]] == 'OOO': fill_o += 1
    if count_x-count_o == 1 and fill_o == 0 and fill_x <= 2: print('yes')
    elif count_x == count_o and fill_x == 0 and fill_o <= 1: print('yes')
    else: print('no')
    sys.stdin.readline()