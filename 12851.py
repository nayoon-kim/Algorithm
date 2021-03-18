import sys
import copy
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * 100001
q = deque()
visited[n] = True
q.append([n, 0, copy.deepcopy(visited)])
result = 999999999
c = 1


while q:
    nn, count, _visited = q.popleft()
   
    _visited[nn] = True

    if nn == k:
        if result == count:
            c += 1
        elif result > count:
            result = count
            c = 1

    nn1 = nn + 1
    nn2 = nn - 1
    nn3 = 2 * nn

    if 0 <= nn1 < 100001 and not _visited[nn1]:
        q.append([nn1, count + 1, _visited])
    if 0 <= nn2 < 100001 and not _visited[nn2]:
        q.append([nn2, count + 1, _visited])
    if 0 <= nn3 < 100001 and not _visited[nn3]:
        q.append([nn3, count + 1, _visited])

print(result)
print(c)