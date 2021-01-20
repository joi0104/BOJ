import sys
prime = [True] * 1000001
prime[0] = prime[1] = False
prime_list = []

for i in range(2, 500001):
    if not prime[i]: continue
    for j in range(i**2, 1000001, i): prime[j] = False
    prime_list.append(i)

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    tmp = 0
    for j in prime_list:
        if j > n//2: break
        if prime[n-j]: tmp +=1
    print(tmp)