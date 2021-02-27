import sys

dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
maxValue = 0
r = 0
c = 0
board = 0

def _ord(x):
    return ord(x) - ord('A')

def dfs(v1, v2, visited, _max):

    global maxValue

    if v1 < 0 or v1 >= r:
        return
    if v2 < 0 or v2 >= c:
        return
    maxValue = max(maxValue, _max)
    
    if visited[_ord(board[v1][v2])] == 0:
        visited[_ord(board[v1][v2])] = 1
        dfs(v1 + 1, v2, visited, _max + 1)
        dfs(v1 - 1, v2, visited, _max + 1)
        dfs(v1, v2 + 1, visited, _max + 1)
        dfs(v1, v2 - 1, visited, _max + 1)
        visited[_ord(board[v1][v2])] = 0


def start():
    global r
    global c
    global board

    r, c = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(r)]

    visited = [0] * 26

    dfs(0, 0, visited, 0)

    print(maxValue)

    

start()
    