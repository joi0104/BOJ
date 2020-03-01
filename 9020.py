n=10000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for i in range(int(input())):
    n = int(input())
    for i in range(1,n//2+1):
        temp = n//2+1-i
        if temp in primes and n-temp in primes:
            print(temp, n-temp)
            break


