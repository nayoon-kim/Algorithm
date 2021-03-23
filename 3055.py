import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

_map = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[-1] * c for _ in range(r)]

def bfs(i, j):
    visited[i][j] = 0
    
    queue = deque()
    for z in range(r):
        for zz in range(c):
            if _map[z][zz] == '*':
                queue.append([z, zz, '*'])
    queue.append([i, j, 'S'])
    result = 'KAKTUS'

    while queue:
        _x, _y, who = queue.popleft()
        
        for i in range(4):
            x = _x + dx[i]
            y = _y + dy[i]

            if x < 0 or x >= r or y < 0 or y >= c: continue
            if _map[x][y] == 'X': continue
            if _map[x][y] == '*': continue
            if who == '*':
                if _map[x][y] == 'D': continue
                _map[x][y] = '*'
                queue.append([x, y, '*'])
            else:
                if visited[x][y] != -1: continue
                visited[x][y] = visited[_x][_y] + 1
                if _map[x][y] == 'D':
                    result = visited[x][y]
                    break

                _map[x][y] = '.'
                _map[x][y] = 'S'
                queue.append([x, y, 'S'])
    return result

r_x, r_y = 0, 0
for i in range(r):
    for j in range(c):
        if _map[i][j] == 'S':
            r_x = i
            r_y = j
            break
print(bfs(r_x, r_y))