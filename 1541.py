t = [sum(map(int,i.split('+'))) for i in input().split('-') ]
print(t[0]-sum(t[1:]))