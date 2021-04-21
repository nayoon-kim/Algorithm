import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m_ap = []
l, r, c = 0, 0, 0
s1, s2, s3 = 0, 0, 0
e1, e2, e3 = 0, 0, 0

def bfs():
    q = deque()
    visited = [[[-1] * c for __ in range(r)] for _ in range(l)]
    visited[s1][s2][s3] = 0
    q.append([s1, s2, s3])

    while q:
        _x, _y, _z = q.popleft()
        
        if _x == e1 and _y == e2 and _z == e3:
            return visited[e1][e2][e3]

        for i in range(6):
            x = dx[i] + _x
            y = dy[i] + _y
            z = dz[i] + _z
            if x < 0 or y < 0 or z < 0 or x >= l or y >= r or z >= c: continue
            if m_ap[x][y][z] == '#': continue
            if visited[x][y][z] != -1: continue
            # print(x, y, z, visited[x][y][z])
            # for j in range(l):
            #     for k in range(r):
            #         print(visited[j][k])
            #     print()
            visited[x][y][z] = visited[_x][_y][_z] + 1
            q.append([x, y, z])

    return -1

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0: break
    
    target = 0
    m_ap = []
    for __ in range(l):
        target += 1
        a = []
        for _ in range(r):
            a.append(list(input().rstrip()))
        m_ap.append(a)
        if target < l:
            input()
    # print(m_ap)
    s1, s2, s3 = 0, 0, 0
    e1, e2, e3 = 0, 0, 0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if m_ap[i][j][k] == 'S':
                    s1, s2, s3 = i, j, k
                if m_ap[i][j][k] == 'E':
                    e1, e2, e3 = i, j, k
    
    result = bfs()
    if result == -1: print("Trapped!")
    else: print("Escaped in", result, "minute(s).")
    input()
