N = int(input())
tmp = [0,0,0,0,0,0,0,0,0,0]
arr = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    for j in range(10):
        if j == 0:
            tmp[j] = arr[1]
        elif j == 9:
            tmp[j] = arr[8]
        else:
            tmp[j] = arr[j - 1] + arr[j + 1]
    tmp , arr = arr, tmp

print(sum(arr)%1000000000)