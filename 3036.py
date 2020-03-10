import fractions
n = int(input())
t = list(map(int,input().split()))
first,t = t[0],t[1:]
for i in t:
    tmp = fractions.Fraction(i,first)
    print(str(tmp.denominator)+'/'+str(tmp.numerator))