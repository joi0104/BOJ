n,m = map(int,input().split())
table= [input() for _ in range(n)]
k = int(input())
answer = [0]*n
for row in range(n):
    count_0 = len(list(filter(lambda x: x == '0', table[row])))
    if count_0 <= k and (count_0%2)==(k%2):
        for another_row in range(n):
            if table[row] == table[another_row]: answer[row] += 1
print(max(answer))