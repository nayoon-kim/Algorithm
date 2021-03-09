from collections import deque

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]
answer = list()
visited = []
w = 0
h = 0
ls = []

def bfs(i, j):
    global visited
    queue = deque([[i, j]])

    while queue:
        x, y = queue.pop()
        
        visited[x][y] = True
    
        for i in range(8):
            _x = x + dx[i]
            _y = y + dy[i]

            if -1 < _x < h and -1 < _y < w and ls[_x][_y] == 1 and not visited[_x][_y]:
                queue.append([_x, _y])

def dfs(x, y):
    global visited

    visited[x][y] = True
    
    for i in range(8):
        _x = x + dx[i]
        _y = y + dy[i]

        if -1 < _x < h and -1 < _y < w and ls[_x][_y] == 1 and not visited[_x][_y]:
            dfs(_x, _y)
        

def main_task():
    global visited
    visited = [[False] * w for i in range(h)]
    land = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and ls[i][j] == 1:
                dfs(i, j)
                land += 1
    
    return land

while True:
    
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        for a in answer:
            print(a)
        break

    ls = list()
    for _ in range(h):
        ls.append(list(map(int, input().split())))

    answer.append(main_task())