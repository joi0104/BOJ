n, k = map(int, input().split())
n_f, k_f, n_k_f = 1, 1, 1
m = 1000000007

for i in range(2, n+1):
    n_f *= i
    n_f %= m
    if i == k: k_f = n_f
    if i == n-k: n_k_f = n_f

print(int(n_f/(k_f*n_k_f)) % m)