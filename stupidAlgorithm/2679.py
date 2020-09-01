def set_flow(prv):
    flow, cur = float('inf'), N - 1
    while cur != 0:
        flow, cur = min(flow, C[prv[cur]][cur] - F[prv[cur]][cur]), prv[cur]
    cur = N - 1
    while cur != 0:
        F[prv[cur]][cur] += flow
        F[cur][prv[cur]] -= flow
        cur = prv[cur]
    asr.append(flow)
    return

def dfs(cur, prv):
    if cur == N - 1:
        set_flow(prv)
    for next in adj[cur]:
        if C[cur][next] >= F[cur][next] and prv[next] < 0:
            prv[next] = cur
            dfs(next, prv[:])
            prv[next] = 0
    return

T = int(input())
N, E, A, B = map(int, input().split())
F = [[0] * N for _ in range(N)]
C = [[0] * N for _ in range(N)]
adj = [set() for _ in range(N)]
asr = []

for _ in range(E):
    U, V, W = map(int, input().split())
    C[U][V] += W
    adj[U].add(V)
    adj[V].add(U)

dfs(0, [-1] * N)
print(asr)
