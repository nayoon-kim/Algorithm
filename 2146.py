from collections import deque
import copy

n = int(input())
table = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * n for _ in range(n)]
land = 1
result = 200
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, land):
    queue = deque([[x, y]])
    table[x][y] = land
    visited[x][y] = True
    while queue:
        x, y = queue.pop()
        
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]

            if -1 < _x < n and -1 < _y < n and table[_x][_y] == 1 and not visited[_x][_y]:
                visited[_x][_y] = True
                table[_x][_y] = land
                queue.appendleft([_x, _y])

def land_bfs(c):
    global result
    queue = deque()
    v = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if table[i][j] == c:
                queue.append([i, j])
                v[i][j] = 0
    
    while queue:
        x, y = queue.pop()
        
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]

            if -1 < _x < n  and -1 < _y < n and table[_x][_y] != c:
                if table[_x][_y] != 0:
                    result = min(result, v[x][y])
                    return
                v[_x][_y] = v[x][y] + 1
                queue.appendleft([_x, _y])
    return n

def task():
    global land
    global result
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j] == 1:
                land += 1
                bfs(i, j, land)

    v = [[False] * n for _ in range(n)]
    total_min =  200

    for i in range(2, land + 1):
        land_bfs(i)
    print(result)
task()
