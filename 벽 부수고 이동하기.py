import queue
import copy

answer = False

# point 각각의 경로에 대해서 방문여부를 기록한다.

def bfs(q, str, n, m):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    global answer

    _q = queue.Queue()
    while q.empty() == False:
        p = q.get()
        for d in dir:
            if p[0] + d[0] == n - 1 and p[1] + d[1] == m - 1:
                answer = True
            if p[0] + d[0] > -1 and p[0] + d[0] < n and p[1] + d[1] > -1 and p[1] + d[1] < m:
                if p[3][p[0]+d[0]][p[1]+d[1]] == 0:
                    p[3][p[0]+d[0]][p[1]+d[1]] = 1
                    if str[p[0] + d[0]][p[1] + d[1]] == 0:
                        _q.put([p[0]+d[0], p[1]+d[1], p[2], p[3]])
                    if str[p[0] + d[0]][p[1] + d[1]] == 1:
                        if p[2] == 0:
                            _q.put([p[0]+d[0], p[1]+d[1], p[2] + 1, p[3]])
    return _q


a = input().split(' ')
n, m = int(a[0]), int(a[1])

str = []
for i in range(0, n):
    str.append(list(input()))

for i in range(0, n):
    for j in range(0, m):
        str[i][j] = int(str[i][j])

temp = [[0] * m for i in range(0, n)]

q = queue.Queue()
q.put([0, 0, 0, temp])

min = 1

while True:
    if answer:
        print(min)
        break
    else:
        q = bfs(q, str, n, m)

        if q.empty() == True:
            print(-1)
            break
        min+=1
