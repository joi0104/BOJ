def zipper(x,y,n):
    global answer

    if check_same(x,y,n):
        answer += video[x][y]
        return

    answer += '('
    zipper(x,y,n//2)
    zipper(x,y+ n//2,n//2)
    zipper(x+n//2,y,n//2)
    zipper(x+n//2,y+n//2,n//2)
    answer += ')'

def check_same(x,y,n):
    tmp = video[x][y]
    for i in range(n):
        for j in range(n):
            if video[x+i][y+j] != tmp : return False
    return True

n = int(input())
video = [input() for _ in range(n)]
answer = ''
zipper(0,0,n)
print(answer)