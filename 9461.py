p = [1,1,1,2,2,3,4,5]
for i in range(8,100): p.append(p[i-1]+p[i-5])
for _ in range(int(input())): print(p[int(input())-1])