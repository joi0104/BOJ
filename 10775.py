import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
gate = [0] * g

for _ in range(p):
    gi = int(input())
    if sum(gate[:gi]) >= gi:
        print(sum(gate))
        exit()
    gate[gi - 1] += 1

print(sum(gate))
