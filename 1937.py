# We have to make him live longer

# bamboo
n = int(input())

# forest
fr = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]
def bfs(i, j):
    visited = [[False] * n for _ in range(n)]
    queue = deque([[i, j, 1]])
    _max = 0
    while queue:
        x, y, m = queue.popleft()
        
        if _max < m :
            _max = m

        for i in range(4):
            if -1< x + xx[i] < n and -1 < y + yy[i] < n:
                if visited[x+xx[i]][y+yy[i]] is False and fr[x][y] < fr[x+xx[i]][y+yy[i]]:
                    queue.append([x+xx[i], y+yy[i], m + 1])
                    visited[x+xx[i]][y+yy[i]] = True
    
    return _max

_max = 0

for i in range(n):
    for j in range(n):
        result = bfs(i, j)
        if result > _max:
            _max = result

print(_max)

# memoization
# 주어진 입력값에 대한 결과를 저장함으로써 같은 입력값에 대해 함수가 한 번만 실행되는 것을 보장한다.
# memo를 해서 반복되는 결과를 메모리에 저장해놓고 다음에 같은 결과가 나올 때 다시 계산할 필요없이 빨리 실행하는 기법
# 일종의 캐싱
