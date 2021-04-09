import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
visited = [INF] * (n + 1)
visited_graph = [0] * (n + 1)
graph = dict()
q = []

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

heapq.heappush(q, (0, 1))
visited[1] = 0

while q:
    dist, now = heapq.heappop(q)
    
    for info in graph[now]:
        
        cost = dist + info[1]
        if visited[info[0]] > cost:
            visited[info[0]] = cost
            visited_graph[info[0]] = (max(now, info[0]), min(now, info[0]))
            heapq.heappush(q, (cost, info[0]))


answer = 0 
for _ in visited_graph:
    if _ != 0:
        answer += 1
print(answer)
for vg in visited_graph:
    if vg != 0:
        print(vg[0], vg[1])