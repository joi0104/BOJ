N,M = map(int,input().split())
team_mem,mem_team = {},{}

for i in range(N):
    team_name,mem_num = input(),int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        mem_name = input()
        team_mem[team_name].append(mem_name)
        mem_team[mem_name] = team_name

for i in range(M):
    mem_or_team_name, tmp = input(), int(input())
    if tmp:
        print(mem_team[mem_or_team_name])
    else :
        for j in sorted(team_mem[mem_or_team_name]):
            print(j)
