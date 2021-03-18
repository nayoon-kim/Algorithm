import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

frame = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(_x, _y):
    for i in range(4):
        x = _x + dx[i]
        y = _y + dy[i]

        if 0 <= x < n and 0 <= y < m and not visited[x][y] and frame[x][y] == '0':
            visited[x][y] = True
            dfs(x, y)
            

def bfs(_x, _y):
    q = deque()
    q.append([_x, _y])
    visited[_x][_y] = True

    while q:
        xx, yy = q.popleft()

        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if 0 <= x < n and 0 <= y < m and not visited[x][y] and frame[x][y] == '0':
                visited[x][y] = True
                q.append([x, y])

ice_cream = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and frame[i][j] == '0':
            ice_cream += 1
            visited[i][j] = True
            dfs(i, j)
            
print(ice_cream)

