countA, countB, maxA, maxB = map(int, input().split())
answer = 0

if countA > countB:
    countA, countB, maxA, maxB = countB, countA, maxB, maxA

if countA == 0 or maxA == 0:
    answer = maxB if maxB < countB else countB
elif countB == 0 or maxB == 0:
    answer = maxA if maxA < countA else countA
elif countA == countB:
    answer += (countA * 2)
else:
    n = countA + 1
    answer += (countA + n)
    countB -= n
    answer += ((maxB-1)*n) if (countB//n) >= (maxB -1) else countB
print(answer)