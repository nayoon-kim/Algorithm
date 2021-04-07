import sys
import heapq
input = sys.stdin.readline

tc = int(input())
INF = int(1e9)

for _ in range(tc):
    n, d, c = map(int, input().split())
    dp = dict()
    for i in range(1, n + 1):
        dp[i] = []
    
    for i in range(d):
        a, b, s = map(int, input().split())
        dp[b].append((a, s))
    
    visited = [INF] * (n + 1)
    
    q = []
    heapq.heappush(q, (0, c))
    visited[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        # print(dist, now, dp[now])
        for aa in dp[now]:
            cost = aa[1] + dist
            # print(aa, cost)
            if cost < visited[aa[0]]:
                visited[aa[0]] = cost
                heapq.heappush(q, (cost, aa[0]))
    # print(visited)
    answer1 = n
    answer2 = 0
    for v in visited[1:]:
        if v == INF:
            answer1 -= 1
        else:
            answer2 = max(answer2, v)
    print(answer1, answer2)    
        
        