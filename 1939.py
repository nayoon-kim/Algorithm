import sys
from collections import deque

def limit(n, bridges, factory1, factory2):
    queue = deque([[factory1, 0, [False]*n]])
    _max = 0
    while queue:
        q = queue.popleft()
        # print(q)

        if q[0] == factory2:
            if _max < q[1]:
                _max = q[1]

        for i, b in enumerate(bridges[q[0]]):
            if q[2][i] == False:
                q[2][i] = True
                if q[1] < b:
                    q[1] = b
                queue.append([i+1, q[1], q[2]])
                
    return _max

def start():
    n, m = map(int, sys.stdin.readline().split())
    
    info = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    
    factory1, factory2 = map(int, sys.stdin.readline().split())

    bridges = dict()
    for _n in range(n):
        bridges[_n+1] = []
        
    for i in info:
        if bridges[i[0]][i[1]-1] < i[2]:
            bridges[i[0]][i[1]-1].append([i[1]-1,i[2]])
        if bridges[i[1]][i[0]-1] < i[2]:
            bridges[i[1]][i[0]-1].append([i[0]-1,i[2]])
    print(bridges)
    # print(limit(n,bridges, factory1, factory2))

    

start()