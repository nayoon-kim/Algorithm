import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().rstrip().split())

gym = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
visited = [[0] * m for _ in range(n)]
q = deque()
q.append((x1 - 1, y1 - 1))

while visited[x2 - 1][y2 - 1] == 0:
    if not q:
        break
    _x, _y = q.popleft()

    for i in range(4):
        for j in range(1, k + 1):
            x = _x + dx[i] * j
            y = _y + dy[i] * j
            
            # 한 쪽 방향으로 가는 도중에 하자가 있으면 얼만큼을 가든 쭉 못 감
            if x < 0 or x >= n or y < 0 or y >= m: break
            # 벽있으면 쭉 못 감
            if gym[x][y] == '#': break
            # 방문했던 곳의 횟수가 방문할 곳의 횟수보다 크면 갈 이유가 없음. 쭉 가는 것도 마찬가지
            if visited[x][y] != 0 and visited[x][y] <= visited[_x][_y]: break
            # 방문한 적은 있음. 다만 좀 더 쭉 가볼 필요가 있음.
            if visited[x][y] != 0: continue
            visited[x][y] = visited[_x][_y] + 1
            q.append((x, y))
if visited[x2 - 1][y2 - 1] == 0:
    visited[x2 - 1][y2 - 1] = -1
print(visited[x2 - 1][y2 - 1])