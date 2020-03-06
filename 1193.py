x,i= int(input()),0
while  x-(i+1) > 0 : x,i = x-(i+1),i+1
answer = [0,i]
while x>1: answer, x = [answer[0]+1,answer[1]-1], x-1
if not i%2 : answer[0],answer[1] = answer[1],answer[0]
print(str(answer[0]+1)+'/'+str(answer[1]+1))