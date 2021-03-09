from collections import deque

skills = input().split()
n = int(input())
    
adj = {}
result = []
cs = {}
for s in skills:
    adj[s] = []
    cs[s] = False
    
for _n in range(n):
    x, y = input().split()
    adj[x].append(y)

def func(p):
    q = deque([[p]])


    while q:
        
        a = q.pop()
        target = a[-1]
        
        if adj[target] != []:
            for _ in adj[target]:
                cs[_] = True
                q.append(a + [_])
        else:
            if len(a) > 1:
                result.append(a)
        
for a in adj:
    for _ in a:
        if not cs[_]:
            func(_)
print(result)