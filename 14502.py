import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

e = [] # empty
v = [] # virus
for i in range(n):
    for j in range(m):
        if table[i][j] == 2:
            v.append([i, j])
        elif table[i][j] == 0:
            e.append([i, j])

# 빈 곳 중 3개를 골라 조합으로 만든다.
e = list(combinations(e, 3))

def bfs(ee):
    s = deepcopy(table)
    result = 0
    for a, b in ee:
        s[a][b] = 1
    q = deque()
    for i in v:
        q.append(i)
    
    while q:
        _x, _y = q.popleft()
        # print(_x, _y)
        for i in range(4):
            x = _x + dx[i]
            y = _y + dy[i]

            if x < 0 or y < 0 or x >= n or y >= m: continue
            if s[x][y] == 1 or s[x][y] == 2: continue
            s[x][y] = 2
            q.append([x, y])

    for i in range(n):
        for j in range(m):
            if s[i][j] == 0:
                result += 1
    return result
    
minimum = 0
for ee in e:
    minimum = max(minimum, bfs(ee))
print(minimum)
