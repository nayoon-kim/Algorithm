import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def outside():
    visited = [[False] * m for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    num = 0
    while q:
        _x, _y = q.popleft()
        
        for i in range(4):
            x = _x + dx[i]
            y = _y + dy[i]

            if x < 0 or y < 0 or x >= n or y >= m: continue
            if visited[x][y]: continue

            visited[x][y] = True
            if s[x][y] == 1:
                s[x][y] = 2
                num += 1
            elif s[x][y] == 0:
                q.append((x, y))
    return num

def bfs(a, b):
    visited = [[False] * m for _ in range(n)]
    qq = deque()
    qq.append((a, b))
    visited[a][b] = True
    answer = 1
    s[a][b] = 0
    while qq:
        _x, _y = qq.popleft()

        for i in range(4):
            x = _x + dx[i]
            y = _y + dy[i]

            if x < 0 or y < 0 or x >= n or y >= m: continue
            if visited[x][y]: continue
            visited[x][y] = True
            if s[x][y] == 0: continue
            if s[x][y] == 2:
                s[x][y] = 0
                answer += 1
            qq.append((x, y))
    return answer
answer = 0
time = 0
while True:
    num = outside()
    temp = 0
    if num == 0:
        print(time)
        print(answer)
        break

    for i in range(n):
        for j in range(m):
            if s[i][j] == 2:
                temp += bfs(i, j)
                
    answer = temp
    time += 1