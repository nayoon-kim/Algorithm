from collections import deque

f, s, g, u, d = map(int, input().split())

r = [u, -d]

visited = [False] * (f + 1)

q = deque([[s, 0]])

answer = -1

visited[s] = True
while q:
    p, c = q.pop()
    
    if p == g:
        answer = c
        break

    for i in r:
        _p = p + i
        
        if 0 < _p < f + 1 and not visited[_p]:
            visited[_p] = True
            q.appendleft([_p, c + 1])
            

print(answer) if answer != -1 else print("use the stairs")