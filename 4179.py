import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
table = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
jx, jy= 0, 0 # J는 입력에서 하나만 주어진다.
fire = [] # 

def bfs():
    
    qq = deque()
    # movements, x, y
    qq.append([0, jx, jy])
    visited[jx][jy] = True

    ffq = deque()
    for fx, fy in fire:
        # x, y
        ffq.append([fx, fy]) 
   
    while qq:
        fq = ffq
        q = qq
        ffq = deque()
        qq = deque()
 
        while fq:
            _fx, _fy = fq.popleft()
            
            for i in range(4):
                ffx = _fx + dx[i]
                ffy = _fy + dy[i]

                if ffx < 0 or ffy < 0 or ffx >= r or ffy >= c: continue
                if table[ffx][ffy] == '#' or table[ffx][ffy] == 'F': continue
                table[ffx][ffy] = 'F'
                ffq.append([ffx, ffy])
        while q:
            movements, _x, _y = q.popleft()

            if _x == 0 or _y == 0 or _x == r - 1 or _y == c - 1:      
                return movements + 1
                
            for i in range(4):
                x = _x + dx[i]
                y = _y + dy[i]

                if x < 0 or y < 0 or x >= r or y >= c: continue
                if table[x][y] == '#' or table[x][y] == 'F': continue
                if visited[x][y]: continue
                visited[x][y] = True # '7% 틀렸습니다' 원인, 지훈이 방문체크 안하면 7%
                qq.append([movements + 1, x, y])

    return "IMPOSSIBLE"

for i in range(r):
    for j in range(c):
        if table[i][j] == 'J':
            jx, jy = i, j
            table[i][j] = '.'
        if table[i][j] == 'F':
            fire.append([i, j])

print(bfs())