
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

info = []
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(0, m):
    a, b = map(int, input().split())
    # info.append([a[0], a[1]])
    # info.append([a[1], a[0]])
    adj[a].append(b)
    adj[b].append(a)

def dfs(p):
    visited[p] = True
    for e in adj[p]:
        if not visited[e]:
            dfs(e)
    # for i in info:
    #     if i[0] == p and not visited[i[1]]:
    #         dfs(i[1])

elem = 0
print(adj)
for _ in range(1, n + 1):
    if not visited[_]:
        elem += 1
        dfs(_)

print(elem)