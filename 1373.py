n = input()
answer = ''
for i in range(len(n),-1,3):
    tmp = 0
    for j,k in [[i,1],[i+1,2],[i+2,4]]:
        try: tmp += (int(n[j])*k)
        except: break
    answer += str(tmp)
print(answer[::-1])


