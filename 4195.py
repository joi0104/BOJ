def find(a):
    if parents[a] == a:
        return a
    tmp = find(parents[a])
    parents[a] = tmp
    return tmp

def union(a, b):
    p_a, p_b = find(a), find(b)
    if p_a != p_b:
        parents[p_b] = p_a
        count[p_a] += count[p_b]

for _ in range(int(input())):
    network = []
    parents = {}
    count = {}

    for _ in range(int(input())):
        a, b = input().split()
        network.append([a, b])
        parents[a], parents[b] = a, b
        count[a], count[b] = 1, 1

    for c in network:
        a, b = c
        union(a, b)
        print(count[find(a)])
