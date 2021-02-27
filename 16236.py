import sys
from collections import deque
d = [0, 0, 1, -1]
dd = [1, -1, 0, 0]

def bfs(n, status):
    baby_shark = []
    fish = [0] * 7
    for i, s in enumerate(status):
        for j, _ in enumerate(s):
            if _ == 9:
                baby_shark = [i, j, 2]
            elif _ != 0:
                fish[_] += 1
    
    queue = deque([baby_shark])

    while queue:
        q = queue.popleft()
        
        for _ in range(4):
            x = q[0] + d[_]
            y = q[1] + dd[_]
            w = q[2]

            if -1 < x < n and -1 < y < n:
                


def start():
    n = int(sys.stdin.readline())
    status = []
    for _ in range(n):
        status.append(list(map(int, sys.stdin.readline().split())))


    bfs(n, status)


start()