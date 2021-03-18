import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

fight = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * n for _ in range(m)]

def bfs(_x, _y):
    q = deque()
    q.append([_x, _y])
    visited[_x][_y] = True
    count = 0
    flag = fight[_x][_y]
    while q:
        xx, yy = q.popleft()
        count += 1

        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                if fight[x][y] == flag:
                    q.append([x, y])
                    visited[x][y] = True
    return count

W = 0
B = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            a = bfs(i, j)
            if fight[i][j] == 'W':
                W += a**2
            else:
                B += a**2
print(W,B)
