nums = []
while not nums or nums[-1] != 0: nums.append(int(input()))
n = max(nums)
prime = [0,0]+[2]*(n-1)
for i in range(2,n+1):
    if prime[i] == 0: continue
    elif prime[i] == 2:
        prime[i],j = 1,2
        while i*j < n+1: prime[i*j],j = 0,j+1
for i in nums:
    for j in range(2,n//2):
        if prime[2*j-1] == 1 and prime[i-2*j+1] == 1 :
            print(i,'=',2*j-1,'+',i-2*j+1)
            break
