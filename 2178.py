import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

table = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = n * m

def dfs(_x, _y, count): 
    global result
    visited[_x][_y] = True
    if _x == n - 1 and _y == m - 1:
        result = min(result, count)

    for i in range(4):
        x = _x + dx[i]
        y = _y + dy[i]

        if 0 <= x < n and 0 <= y < m and not visited[x][y] and table[x][y] == 1:
            dfs(x, y, count + 1)
        
dfs(0, 0, 1)

print(result)