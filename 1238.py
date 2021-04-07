import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)
INF = int(1e9)
distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n + 1):
    q = []
    
    # start node i
    distance[i][i] = 0
    
    heapq.heappush(q, (0, i))
    while q:
        dist, now = heapq.heappop(q)
        if distance[i][now] < dist: continue
        
        for g in graph[now]:
            if distance[i][g[0]] > dist + g[1]:
                distance[i][g[0]] = distance[i][now] + g[1]
                heapq.heappush(q, (distance[i][g[0]], g[0]))


for i in range(1, n + 1):
    answer[i] += distance[i][x] + distance[x][i]

print(max(answer))
    
