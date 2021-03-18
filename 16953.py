import sys
from collections import deque
import heapq

a, b = map(int, sys.stdin.readline().rstrip().split())

mn = 1
mx = 1000000001

visited = {}

def bfs(n):
    q = []
    heapq.heappush(q, (0, n))

    result = 999999999
    while q:
        count, x = heapq.heappop(q)
        # print(x, count)
        visited[x] = True

        if x == b:
            result = count + 1
            break

        x1 = x * 2
        x2 = x * 10 + 1

        if mn <= x1 < mx and not x1 in visited.keys():
            heapq.heappush(q, (count + 1, x1))
        if mn <= x2 < mx and not x2 in visited.keys():
            heapq.heappush(q, (count + 1, x2))
    if result == 999999999:
        result = -1
    return result

print(bfs(a))