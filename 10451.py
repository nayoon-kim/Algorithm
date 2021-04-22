import sys
from collections import deque
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    cycle_input = list(map(int, input().split()))
    cycle = dict()
    for idx, i in enumerate(cycle_input):
        cycle[idx + 1] = i
    
    visited = [0] * (n + 1)
    cnt = 1
    for i in cycle:
        if visited[i] == 0:
            q = deque([i])
            visited[i] = cnt
            while q:
                cur = q.popleft()
                
                if visited[cycle[cur]] != 0: continue
                visited[cycle[cur]] = cnt
                q.append(cycle[cur])
            cnt += 1
    print(cnt-1)

    