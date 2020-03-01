for i in range(int(input())):
    tmp = list(map(int,input().split()))
    evg = sum(tmp[1:])/tmp[0]
    tmp2 = [i for i in tmp[1:] if i > evg]
    print('%.3f%%' %(len(tmp2)/tmp[0]*100))
