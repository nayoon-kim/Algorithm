from collections import deque
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
testcase = int(input())
answer = list()
for t in range(testcase):
    l = int(input())
    cur = list(map(int, input().split()))
    fut = list(map(int, input().split()))

    queue = deque()
    queue.append(cur)
    visited = [[-1] * l for _ in range(l)]
    visited[cur[0]][cur[1]] = 0
    while queue:
        _x, _y = queue.popleft()

        for i in range(8):
            x = _x + dx[i]
            y = _y + dy[i]

            if 0 <= x < l and 0 <= y < l:
                if visited[x][y] == -1 or visited[x][y] > visited[_x][_y] + 1:
                    visited[x][y] = visited[_x][_y] + 1
                    queue.append([x, y])
    answer.append(visited[fut[0]][fut[1]])

for a in answer:
    print(a)