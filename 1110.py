N = int(input())
tmp = N % 10 * 10 + (N // 10 + N % 10) % 10
count = 1
while N != tmp :
    tmp = tmp % 10 * 10 + (tmp // 10 + tmp % 10) % 10
    count += 1
print(count)