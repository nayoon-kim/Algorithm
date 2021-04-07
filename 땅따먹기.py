# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# import sys

# r, c, n, m = map(int, sys.stdin.readline().rstrip().split())
# m_ap = [[0] * c for _ in range(r)]
# answer = [0] * (n + 1)
# visited = [[False] * c for _ in range(r)]
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# for _ in range(m):
# 	t = list(map(int, sys.stdin.readline().rstrip().split()))
# 	if t[0] == 2:
# 		m_ap[t[1]][t[2]] = t[3]
# 	else:
# 		m_ap[t[3]][t[4]] = m_ap[t[1]][t[2]]

# def dfs(a, b):
#     visited[a][b] = True

#     for _ in range(4):
#         x = a + dx[_]
#         y = b + dy[_]

#         if x < 0 or y < 0 or x >= r or y >= c: continue

#         if not visited[x][y] and m_ap[a][b] == m_ap[x][y]:
#             dfs(x, y)

# for i in range(1, n + 1):
#     for a in range(r):
#         for _a in range(c):
#             if m_ap[a][_a] == i and not visited[a][_a]:
#                 answer[i] += 1
#                 dfs(a, _a)
# string_answer = ''
# for i in range(1, n + 1):
#     string_answer += str(answer[i]) + ' '
# print string_answer
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

r, c, n, m = map(int, sys.stdin.readline().rstrip().split())
m_ap = [[0] * r for _ in range(c)]
answer = [0] * (n + 1)
visited = [[False] * r for _ in range(c)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(m):
	t = list(map(int, sys.stdin.readline().rstrip().split()))
	if t[0] == 2:
		m_ap[t[1]][t[2]] = t[3]
	else:
		m_ap[t[3]][t[4]] = m_ap[t[1]][t[2]]

def dfs(a, b):
    visited[a][b] = True

    for _ in range(4):
        x = a + dx[_]
        y = b + dy[_]

        if x < 0 or y < 0 or x >= c or y >= r: continue

        if not visited[x][y] and m_ap[a][b] == m_ap[x][y]:
            dfs(x, y)

for i in range(1, n + 1):
    for a in range(c):
        for _a in range(r):
            if m_ap[a][_a] == i and not visited[a][_a]:
                answer[i] += 1
                dfs(a, _a)
string_answer = ''
for i in range(1, n + 1):
    string_answer += str(answer[i]) + ' '
print(string_answer)