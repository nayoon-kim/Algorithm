import sys
input = sys.stdin.readline
n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
INF = float('inf')
visited = [False] * n
distances = [INF] * n
def line(a, b):
    x = (a[0] - b[0]) ** 2
    y = (a[1] - b[1]) ** 2

    return round((x + y) ** 0.5, 2)

def get_min_node():
    mnum = INF
    v = 0

    for i in range(n):
        if not visited[i] and distances[i] < mnum:
            mnum = distances[i]
            v = i
    return v

def prim(start):
    distances[start] = 0
    
    for i in range(n):
        node = get_min_node()
        visited[node] = True
        
        for j in range(n):
            l = line(stars[node], stars[j])
            if not visited[j] and l < distances[j]:
                distances[j] = l
prim(0)
print(sum(distances))