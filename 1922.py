import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float('inf')
net = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    net[a][b] = c
    net[b][a] = c

visited = [False] * (n + 1)
distances = [INF] * (n + 1)

# 방문하지 않은 노드의 distance가 가장 작은 노드 찾기
def get_min_node():
    mnum = INF
    v = 0
    for i in range(1, n + 1):
        if not visited[i] and distances[i] < mnum:
            mnum = distances[i]
            v = i
    return v

def prim(start):
    # start vertex를 설정한다.
    # start vertex는 초기 값이며 key 값을 0으로 할당한다.
    distances[start] = 0
    for i in range(1, n + 1):
        node = get_min_node()
        visited[node] = True

        for j in range(1, n + 1):
            if net[node][j] != INF:
                if not visited[j] and net[node][j] < distances[j]:
                    distances[j] = net[node][j]

prim(1) # 어느 vertex에서 출발하든 상관없이 항상 같은 트리가 형성된다.

sum = 0
for i in range(1, n + 1):
    sum += distances[i]
print(sum)