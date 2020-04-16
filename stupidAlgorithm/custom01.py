def minimize(tile):
    tmp = []
    for i in tile:
        if tmp and i == tmp[-1] : continue
        tmp.append(i)
    return tmp

n,m = map(int,input().split())
tile_row, tile_column = [], []
o_count, x_count = 0, 0

for i in range(n): tile_row.append(input().replace(" ", ""))
tile_row = minimize(tile_row)

for i in range(m):
    tmp = ''
    for j in range(len(tile_row)): tmp += tile_row[j][i]
    tile_column.append(tmp)
tile_column = minimize(tile_column)

for i in tile_column:
    for j in i:
        if j == 'O' : o_count += 1
        if j == 'X' : x_count += 1

print(o_count, x_count)