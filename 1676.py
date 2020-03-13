def fec(n):
    if n==0:
        return 1
    return fec(n-1)*n
n =int(input())
answer, n = 0, fec(n)
while n%10 == 0: answer,n = answer+1, n//10
print(answer)