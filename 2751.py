import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = list()

for i in range(n):
    q.append(int(input()))
q.sort()

print('\n'.join(map(str, q)))
# for i in range(n):
#     heapq.heappush(q, int(input()))

# for i in range(n):
#     print(heapq.heappop(q))