from collections import deque
import copy

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
temp_table = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, v):
    global table
    global temp_table
    q = deque([[x, y]])
    v[x][y] = True
    
    while q:
        x, y = q.pop()
        
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            
            if 0 <= _x < n and 0 <= _y < m:
                if table[_x][_y] == 0:
                    temp_table[x][y] -= 1
                elif table[_x][_y] != 0 and not v[_x][_y]:
                    v[_x][_y] = True
                    q.appendleft([_x, _y])

        if temp_table[x][y] < 0:
            temp_table[x][y] = 0

def dfs(x, y, v):
    v[x][y] = True
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        
        if 0 <= _x < n and 0 <= _y < m and table[_x][_y] != 0 and not v[_x][_y]:
            v[_x][_y] = True
            dfs(_x, _y, v)


def task():
    global table
    global temp_table
    time = 1
    while True:
        temp_table = copy.deepcopy(table)
        visited = [[False] * m for _ in range(n)]
        answer = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and table[i][j] != 0:
                    bfs(i, j, visited)
                elif table[i][j] == 0:
                    answer += 1
        land = 0
        table = copy.deepcopy(temp_table)
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and table[i][j] != 0:
                    land += 1
                    dfs(i, j, visited)
        if land >= 2:
            print(time)
            break
    
        time += 1
        
        if answer == n * m:
            print(0)
            break

task()