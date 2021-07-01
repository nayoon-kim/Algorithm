import sys
input = sys.stdin.readline

n, m = map(int, input().split())

r, c, d = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(n)]
vaccuum_area = 0
# north: 0, east: 1, south: 2, west: 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, d, w):
    global vaccuum_area

    if w == 4:
        _x = x - dx[d]
        _y = y - dy[d]
        if 0 <= _x < n and 0 <= _y < m and table[_x][_y] != 1:
            dfs(_x, _y, d, 0)
        return

    # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    # 왼쪽 방향
    dd = d - 1
    if dd == -1: dd = 3
    _x = x + dx[dd]
    _y = y + dy[dd]
    if 0 <= _x < n and 0 <= _y < m:
        # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        if table[_x][_y] == 0:
            # 현재 위치를 청소한다.
            table[_x][_y] = 2
            vaccuum_area += 1
            dfs(_x, _y, dd, 0)
    
        # b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        # 청소할 공간이 없다 = 청소가 이미 되어있거나 벽인 경우
        else:
            # 방향만 바뀐다.
            dfs(x, y, dd, w + 1)
table[r][c] = 2
vaccuum_area += 1
dfs(r, c, d, 0)

# for t in table:
#     print(t)
print(vaccuum_area)