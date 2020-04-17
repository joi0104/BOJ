def cut_paper(x,y,n):
    if check_same(x,y,n):
        count[paper[x][y]] += 1
        return

    for i in range(3):
        for j in range(3):
            cut_paper(x + (n // 3 * i), y + (n // 3 * j), n // 3)


def check_same(x,y,n):
    tmp = paper[x][y]
    for i in range(n):
        for j in range(n):
            if paper[x+i][y+j] != tmp : return False
    return True

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
count = {-1: 0, 0: 0, 1: 0}
cut_paper(0,0,n)
print(count[-1])
print(count[0])
print(count[1])