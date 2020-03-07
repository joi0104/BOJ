f = [0,1]
for i in range(2,int(input())+1): f.append(f[i-1]+f[i-2])
print(f[-1])