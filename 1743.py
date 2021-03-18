import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().rstrip().split())

table = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    table[x-1][y-1] = 1


def bfs(_x, _y):
    q = deque()
    q.append([_x, _y])
    visited[_x][_y] = True
    count = 1
    while q:
        xx, yy= q.popleft()
        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if 0 <= x < n and 0 <= y < m and not visited[x][y] and table[x][y] == 1:
                visited[x][y] = True
                count += 1
                q.append([x, y])

    return count
    

a = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and table[i][j] == 1:
            a= max(a, bfs(i, j))
            
print(a)