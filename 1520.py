import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

route = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return