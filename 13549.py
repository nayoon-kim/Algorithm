import sys
import copy
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100001


def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 0

    while q:
        c = q.popleft()
        
        c1 = c + 1
        c2 = c - 1
        c3 = 2 * c

        if 0 <= c1 < 100001 and (visited[c1] == -1 or (visited[c1] != -1 and visited[c1] > visited[c])):
            visited[c1] = visited[c] + 1
            q.append(c1)
        if 0 <= c2 < 100001 and (visited[c2] == -1 or (visited[c2] != -1 and visited[c2] > visited[c])):
            visited[c2] = visited[c] + 1
            q.append(c2)
        if 0 <= c3 < 100001 and (visited[c3] == -1 or (visited[c3] != -1 and visited[c3] > visited[c])):
            visited[c3] = visited[c]
            q.append(c3)

    return visited[k]


print(bfs(n))