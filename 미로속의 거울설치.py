import sys
from collections import deque

r, c = map(int, sys.stdin.readline().rstrip().split())
m_ap = [list(sys.stdin.readline().rstrip()) for _ in range(c)]
visited = [[-1] * r for _ in range(c)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append([0, 0, 0, 0])
    visited[0][0] = 0
    while queue:

        _x, _y, ddx, ddy = queue.popleft()

        if _x == r - 1 and _y == c - 1:
            print(visited[_x][_y])
            break

        for i in range(4):
            x = _x + dx[i]
            y = _y + dy[i]

            if dx[i] == ddx and dy[i] == ddy: continue

            if x < 0 or y < 0 or x >= r or y >= c: continue

            if m_ap[x][y] == '*': continue
            if visited[x][y] != -1: continue

            if m_ap[x][y] == 'P':
                visited[x][y] = visited[_x][_y] + 1
                queue.append([x, y, dx[i], dy[i]])
            if m_ap[x][y] == '.':
                visited[x][y] = visited[_x][_y] + 1
                queue.append([x, y, 0, 0])
            
    return visited[_x][_y]

print(bfs())