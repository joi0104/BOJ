def cut_paper(x,y,n):
    global count_white
    global count_blue

    if check_same(x,y,n):
        if tile[x][y]: count_blue += 1
        else: count_white += 1
        return

    cut_paper(x,y,n//2)
    cut_paper(x+n//2,y,n//2)
    cut_paper(x,y+n//2,n//2)
    cut_paper(x+n//2,y+n//2,n//2)

def check_same(x,y,n):
    tmp = tile[x][y]
    for i in range(n):
        for j in range(n):
            if tile[x+i][y+j] != tmp : return False
    return True

n = int(input())
tile = [list(map(int, input().split())) for _ in range(n)]
count_white, count_blue = 0,0
cut_paper(0,0,n)
print(count_white)
print(count_blue)