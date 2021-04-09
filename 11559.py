import sys
from collections import deque

input = sys.stdin.readline
game = [list(input().rstrip()) for _ in range(12)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0 # 연쇄

# 하늘에 떠있는 puyo 찾아서 한 줄씩 내려주기
def heap():
    total_change = 0
    
    while True:
        change = 0
        for i in range(10, -1, -1):
            for j in range(6):
                if game[i][j] != '.' and game[i + 1][j] == '.':
                    game[i + 1][j] = game[i][j]
                    game[i][j] = '.'
                    change += 1
        
        if change == 0:
            break
        total_change += change
    return total_change

# 터지기
def bfs(a, b):
    blow = 0
    puyo = game[a][b]
    visited = [[False] * 6 for _ in range(12)]
    q = deque()
    q.append([a, b])
    
    find = deque()
    find.append([a, b])
    visited[a][b] = True

    while q:
        xx, yy = q.popleft()
        
        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if x < 0 or y < 0 or x >= 12 or y >= 6: continue
            if game[x][y] != puyo: continue
            if visited[x][y]: continue

            q.append([x, y])
            find.append([x, y])
            visited[x][y] = True

    if len(find) >= 4:
        blow += 1
        while find:
            x, y = find.popleft()
            game[x][y] = '.'
    return blow

def puyo_puyo():
    global answer

    while True:
        blow = 0
        for i in range(12):
            for j in range(6):
                if game[i][j] != '.':
                    blow += bfs(i, j)

        if blow != 0:
            answer += 1
        if heap() == 0:
            break
    return answer
    
print(puyo_puyo())
    