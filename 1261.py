import sys
from collections import deque
input = sys.stdin.readline

# 가로 크기 m, 세로 크기 n
m, n = map(int, input().split())

# 미로의 상태
maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[-1] * m for _ in range(n)]

# 벽이 없는 방(0)을 이동하는데에는 비용이 0, 부숴야 하는 벽(1)으로 이동하는데에는 비용이 1 소모되는 0과 1의 비용을 가진 탐색
# 비용이 0과 1로 나누어져 있을 때에는 deque를 사용해서 매 노드를 탐색할 때마다 갈 수 있는 노드에 대한 비용이 0이면 앞에, 1이면 뒤에 추가해주며 탐색을 이어나가면 된다.

# 그렇게 하면 비용이 적은 경로부터 우선적으로 탐색하고, 가장 적은 비용에 대한 탐색이 끝나고 나서야 비로소 더 큰 비용의 경로를 탐색하기 시작하기 때문에 벽을 최소한으로 부수고 이동하는 경로를 찾을 수 있게 된다.
def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 0
    while q:
        _x, _y = q.popleft()
        
        for i in range(4):
            x = dx[i] + _x
            y = dy[i] + _y
        
            if x < 0 or y < 0 or x >= n or y >= m: continue
            if visited[x][y] != -1: continue
            if maze[x][y] == 0:
                q.appendleft([x, y])
                visited[x][y] = visited[_x][_y]
            elif maze[x][y] == 1:
                q.append([x, y])
                visited[x][y] = visited[_x][_y] + 1
bfs()
print(visited[n-1][m-1])