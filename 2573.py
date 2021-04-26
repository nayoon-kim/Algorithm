from collections import deque
from copy import deepcopy
import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
temp_table = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if table[i][j] != 0:
                q.append([i, j])
    cnt = 0
    while q:
        fq = q
        q = deque()
        visited = [[False] * m for _ in range(n)]

        while fq:
            a, b = fq.popleft()
            
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]

                if x < 0 or y < 0 or x >= n or y >= m: continue
                if table[x][y] != 0: continue
                table[a][b] -= 1
            
            if table[a][b] > 0:
                q.append([a, b])
            else:
                # 같은 해에 바다가 된 곳은 고려하지 않기 때문에 0이 아닌 -1로 저장한다.
                table[a][b] = -1
        
        # -1을 0으로 바꿔주기
        for i in range(n):
            for j in range(m):
                if table[i][j] == -1:
                    table[i][j] = 0
        cnt += 1
        
        # bfs로 빙산 덩어리 개수 구하기
        counting = 0
        for i in range(n):
            for j in range(m):
                if table[i][j] != 0 and not visited[i][j]:
                    a = deque()
                    a.append([i, j])
                    while a:
                        _x, _y = a.popleft()
                        for aaaa in range(4):
                            xxx = _x + dx[aaaa]
                            yyy = _y + dy[aaaa]
                            
                            if xxx < 0 or yyy < 0 or xxx >= n or yyy >= m: continue
                            if visited[xxx][yyy] == True: continue
                            if table[xxx][yyy] == 0: continue
                            visited[xxx][yyy] = True
                            a.append([xxx, yyy])
                    counting += 1
        # 두 덩어리 이상으로 분리되면 시간 리턴                    
        if counting >= 2:
            print(cnt)
            break
        # 다 녹을 떄까지 분리되지 않으면 0
        if counting == 0:
            print(0)
            break
                
bfs()
                    