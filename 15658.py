def insert_oper(result,num_idx,oper):
    global answer
    if num_idx == n:
        answer.append(result)
        return

    for i in range(4):
        if not oper[i]: continue
        oper[i] -= 1
        if i == 0: insert_oper(result+nums[num_idx],num_idx+1,oper)
        elif i == 1: insert_oper(result-nums[num_idx],num_idx+1,oper)
        elif i == 2: insert_oper(result*nums[num_idx],num_idx+1,oper)
        else:
            if result < 0: insert_oper((abs(result)//nums[num_idx])*-1,num_idx+1,oper)
            else: insert_oper(result//nums[num_idx],num_idx+1,oper)
        oper[i] += 1

n = int(input())
nums = list(map(int,input().split()))
oper = list(map(int,input().split()))
answer = []
insert_oper(nums[0],1,oper)
print(max(answer))
print(min(answer))