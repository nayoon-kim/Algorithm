from collections import deque
import sys
input = sys.stdin.readline

l, w = map(int, input().split())
table = [list(input())[:-1] for _ in range(l)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    c = [[0] * w for _ in range(l)]
    c[x][y] = 1
    num = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < w:
                if table[nx][ny] == 'L' and c[nx][ny] == 0:
                    c[nx][ny] = c[x][y] + 1
                    num = max(num, c[nx][ny])
                    q.append([nx, ny])
    return num - 1

cnt = 0
for i in range(l):
    for j in range(w):
        if table[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))
print(cnt)
