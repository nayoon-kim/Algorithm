# 적록색약

n = int(input())
rg = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    
    color = rg[x][y]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < nx < n and -1 < ny < n :
            if rg[nx][ny] == color and visited[nx][ny]==False:
                dfs(nx, ny)

normal_answer = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            normal_answer+=1

visited = [[False]*n for _ in range(n)]

abnormal_answer = 0
for i in range(n):
    for j in range(n):
        if rg[i][j] == 'R':
            rg[i][j] = 'G'
        
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            abnormal_answer += 1
print(normal_answer)
print(abnormal_answer)