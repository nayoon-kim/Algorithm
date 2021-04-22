import sys
from collections import deque
input = sys.stdin.readline

st_walls = (1, 2, 4, 8)
walls = {0: [], 1: [1], 2: [2], 3: (1, 2), 4: [4], 5: (1, 4), 6: (2, 4), 7: (1, 2, 4), 8: [8], 9: (1, 8), 10: (2, 8), 11: (1, 2, 8), 12: (4, 8), 13: (1, 4, 8), 14: (2, 4, 8), 15: (1, 2, 4, 8)}
opposite_walls = {1: 4, 2: 8, 4: 1, 8: 2}

n, m = map(int, input().split())
m_ap = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(_x, _y, a):
    q = deque()
    q.append([1, _x, _y])
    visited[_x][_y] = a
    result = 0
    while q:
        move, _x, _y = q.popleft()
        
        for sw in st_walls:
            if sw in walls[m_ap[_x][_y]]:continue
            # print("walls[m_ap[",_x,"][",_y,"]]=",walls[m_ap[_x][_y]])
            # print(opposite_walls[sw])
            x = _x
            y = _y
            
            if sw == 1:
                x += dx[0]
                y += dy[0]
            elif sw == 2:
                x += dx[1]
                y += dy[1]
            elif sw == 4:
                x += dx[2]
                y += dy[2]
            else:
                x += dx[3]
                y += dy[3]
            # print("why?", x, y)
            if x < 0 or y < 0 or x >= m or y >= n: continue
            # print("!walls[m_ap[",x,"][",y,"]]=",walls[m_ap[x][y]])

            if opposite_walls[sw] in walls[m_ap[x][y]]: continue
            # print("!!walls[m_ap[",x,"][",y,"]]=",walls[m_ap[x][y]])
            if visited[x][y] != -1: continue
                 
            visited[x][y] = a
            q.append([move + 1, x, y])
    

cnt = 0
r_esult = dict()
# 이 성에 있는 방의 개수
for i in range(m):
    for j in range(n):
        if visited[i][j] == -1:
            bfs(i, j, cnt) 
            cnt += 1
print(cnt)

# 가장 넓은 방의 넓이
for c in range(cnt):
    r_esult[c] = 0
    for i in range(m):
        for j in range(n):
            if c == visited[i][j]:
                r_esult[c] += 1
print(max(r_esult.values()))
# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
re_sult = 0

for i in range(m):
    for j in range(n):
        
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            
            if x < 0 or y < 0 or x >= m or y >= n: continue
            if visited[i][j] == visited[x][y]: continue
            re_sult = max(re_sult, r_esult[visited[i][j]] + r_esult[visited[x][y]])

print(re_sult)