import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
table = [[0] * n for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(k):
    ly, lx, ry, rx = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            table[i][j] = 1
def bfs(_x, _y, c):
    q = deque()
    q.append([_x, _y])
    visited[_x][_y] = c
    while q:
        xx, yy = q.popleft()
        
        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]
            
            if x < 0 or y < 0 or x >= m or y >= n: continue
            if visited[x][y] != -1: continue
            if table[x][y] != 0: continue
            visited[x][y] = c
            q.append([x, y]) 

cnt = 0
for i in range(m):
    for j in range(n):
        if table[i][j] == 0 and visited[i][j] == -1:
            bfs(i, j, cnt)
            cnt += 1

answer = []
for i in range(cnt):
    a = 0
    for k in range(m):
        for j in range(n):
            if visited[k][j] == i:
                a += 1
    answer.append(a)
answer.sort()
print(cnt)
for i in answer:
    print(i, end=' ')

