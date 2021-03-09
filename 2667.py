n = int(input())
p = [list(input()) for i in range(n)]

visited = [[False] * n for i in range(n)]
elem = 0
result = []
dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]
def dfs(i, j):
    visited[i][j] = True
    
    for _ in range(0, 4):
        ax = i + dx[_]
        ay = j + dy[_]
        if -1 < ax < n and -1 < ay < n:
            if not visited[ax][ay] and p[ax][ay] == '1':
                result[elem-1] += 1
                dfs(ax, ay)

            

for i in range(n):
    for j in range(n):
        if p[i][j] == '1' and not visited[i][j]:
            elem += 1
            result.append(1)
            dfs(i, j)

print(elem)
print(sorted(result))