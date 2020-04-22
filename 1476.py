esm = list(map(lambda x: int(x)-1,input().split()))
esm_tmp = [0,0,0]
answer = 1
while True:
    if esm == esm_tmp:
        print(answer)
        break

    answer+=1
    esm_tmp = [(esm_tmp[0]+1)%15,(esm_tmp[1]+1)%28,(esm_tmp[2]+1)%19]