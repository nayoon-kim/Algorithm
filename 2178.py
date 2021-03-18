import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

table = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = n * m

def bfs(_x, _y):
    global result
    q = deque()
    q.append([_x, _y, 1])
    visited[_x][_y] = True
    while q:
        xx, yy, count = q.popleft()

        if xx == n - 1 and yy == m - 1:
            result = min(result, count)

        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if 0 <= x < n and 0 <= y < m and not visited[x][y] and table[x][y] == 1:
                visited[x][y] = True
                q.append([x, y, count + 1])
        
bfs(0, 0)

print(result)