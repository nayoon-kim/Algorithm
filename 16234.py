from collections import deque
n, l, r = map(int, input().split())

visited = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

table = [list(map(int, input().split())) for _ in range(n)]

def bfs(sx, sy):
    move_q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1
    
    population, nation = 0, 0

    while q:
        _x, _y = q.popleft()

        move_q.append([_x, _y])
        population += table[_x][_y]
        nation += 1

        for i in range(4):
            x = _x + dx[i]
            y = _y + dy[i]
            
            if -1 < x < n and -1 < y < n:
                if l <= abs(table[x][y] - table[_x][_y]) <= r and visited[x][y] == 0:
                    visited[x][y] = nation
                    q.append([x, y])

    while move_q:
        mx, my = move_q.popleft()
        table[my][my] = int(population / nation)

    if nation == 1:
        return 0
    return 1

circle = 0
while circle == 0:
    visited = [[0] * n for _ in range(n)]
    a = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                a += bfs(i, j)
    # print(nation)   
    if a == 0:
        break
    circle += 1

print(circle)
