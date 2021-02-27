# n = int(input())
# fr = [list(map(int, input().split())) for _ in range(n)]

# max_live = [[1] * n for _ in range(n)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def dfs(x, y):
#     if max_live[x][y] != 1:
#         return max_live[x][y]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if -1 < nx < n and -1 < ny < n:
#             if fr[x][y] < fr[nx][ny]:
#                 max_live[x][y] = max(max_live[x][y], dfs(nx, ny) + 1)
                
#     return max_live[x][y]

# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans = max(ans, dfs(i, j))

# print(max_live)
# print(ans)

import sys
sys.setrecursionlimit(10**6)

n = int(input())
fr = [list(map(int, input().split())) for i in range(n)]

max_live = [[1] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def print_max_live(x, y):
    print(x, y)
    for i in range(n):
        print(max_live[i])
    print()

def dfs(x, y):
    if max_live[x][y] != 1:
        return max_live[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < n and -1 < ny < n:
            if fr[x][y] < fr[nx][ny]:
                 print_max_live(x, y)
                 max_live[x][y] = max(max_live[x][y], dfs(nx, ny) + 1)
                 print_max_live(x, y)
                 print("done")
                 
    return max_live[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)