import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = dict()
INF = int(1e9)
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    s, d, c = map(int, input().split())
    graph[s].append((d, c))

start, end = map(int, input().split())
visited = [INF] * (n + 1)

q = []
heapq.heappush(q, (0, start))
visited[start] = 0

while q:
    cost, now = heapq.heappop(q)

    for info in graph[now]:
        # info[0]은 도착지점 info[1]은 비용
        t_cost = cost + info[1]
        if t_cost < visited[info[0]]:
            visited[info[0]] = t_cost
            heapq.heappush(q, (t_cost, info[0]))

print(visited[end])