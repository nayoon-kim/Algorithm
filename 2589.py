import sys
from collections import deque
dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(n, m,i,j, maps):
    visited = [[False] * n for _ in range(m)]
    queue = deque([[i, j, visited, 0]])
    _maps = dict()
    while queue:
        q = queue.popleft()
        if _maps["".join([q[0], q[1]])] in _maps:
            _maps["".join([q[0], q[1]])] = min(q[3], _maps["".join[q[0], q[1]]])
        else:
            _maps["".join([q[0], q[1]])] = q[3]
        for d in dd:
            if -1 < q[0] + d[0] < n and -1 < q[1] + d[1] < m and maps[q[0] + d[0]][q[1] + d[1]] == 'L' and not visited[q[0]+d[0]][q[1]+d[1]]:
                visited[q[0]+ d[0]][q[1] + d[1]] = True
                queue.append([q[0]+ d[0], q[1] + d[1], visited, q[3]+1])
                
    print(_maps)    

def start():
    vert, hori = map(int, sys.stdin.readline().split())
    maps = [list(sys.stdin.readline().strip()) for _ in range(vert)]
    
    for i, m in enumerate(maps):
        for j, n in enumerate(m):
            if n == 'L':
                bfs(vert, hori, i, j, maps)

start()