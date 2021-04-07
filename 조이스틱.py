from collections import deque
from copy import deepcopy

def solution(name):
    answer = 0
    queue = deque()
    visited = [[False] for _ in name]
    dd = [1, -1]
    init = 'A' * len(name)
    
    # position, movements
    queue.append([0, upAndDown(name[0]), name[0] + init[1:]])
    visited[0] = True
    result = 987654321
    
    while queue:
        p, m, copied_name = queue.popleft()
        
        if copied_name == name:
            result = min(result, m)
            break
            
        for i in range(2):
            _p = p + dd[i]
            
            if _p == -1: _p = len(name) - 1
            elif _p == len(name):
                _p = 0
            
            if not visited[_p]: continue
            visited[_p] = True
            if _p == len(name) - 1:
                queue.append([_p, m + upAndDown(name[_p]) + 1, copied_name[0:_p] + name[_p]])
            else:
                queue.append([_p, m + upAndDown(name[_p]) + 1, copied_name[0:_p] + name[_p] + copied_name[_p + 1:]])
            
    answer = result
    return answer

def upAndDown(alpha):
    # starts with 'A'
    # go up
    up = ord('Z') - ord(alpha) + 1
    
    # go down
    down = ord(alpha) - ord('A')
    
    return min(up, down)

print(solution("JEROEN"))