import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = dict()

INF = int(1e9)
visited = [INF] * (v + 1)

for i in range(1, v+1):
    graph[i] = []

for _ in range(e):
    u, _v, w = map(int, input().split())
    if graph[u] != [] and graph[u][0] == _v:
        if graph[u][1] > w:
            graph[u][1] = w
    else:
        graph[u].append([_v, w])

q = []
heapq.heappush(q, (0, start))
visited[start] = 0

while q:
    cost, now = heapq.heappop(q)
    
    for info in graph[now]:
        c = cost + info[1]
        
        if c < visited[info[0]]:
            visited[info[0]] = c
            heapq.heappush(q, [c, info[0]])

for v in visited[1:]:
    if v == INF:
        print('INF')
        continue
    print(v)