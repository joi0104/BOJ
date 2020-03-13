def counting(n,i):
    answer = 0
    while n!=0:
        n,answer = n//i, answer+(n//i)
    return answer

n,k = map(int,input().split())
print(min(counting(n,2)-counting(k,2)-counting(n-k,2),counting(n,5)-counting(k,5)-counting(n-k,5)))