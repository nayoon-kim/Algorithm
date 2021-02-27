import sys
from collections import deque

def bfs(computer, network, status):
    answer = 0
    visited = [False] * (computer + 1)
    
    visited[1] = True
    queue = deque([1])
    
    while queue:
        q = queue.popleft()
        for _q in status[q]:
            if not visited[_q]:
                queue.append(_q)
                visited[_q] = True
    
    for i, v in enumerate(visited):
        if v == True:
            answer += 1
    answer -= 1
    return answer
    
def start():
    computer = int(sys.stdin.readline())
    network = int(sys.stdin.readline())
    status = {}
    for _ in range(network):
        i, j = map(int, sys.stdin.readline().split())
        if i in status.keys():
            status[i].append(j)
        else:
            status[i] = [j]
        if j in status.keys():
            status[j].append(i)
        else:
            status[j] = [i]
    
    print(bfs(computer, network, status))

start()