import sys
import heapq
input = sys.stdin.readline

# 상하좌우로 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = int(1e9)
testcase = 0

while True:
    testcase += 1
    n = int(input())
    
    # 입력으로 0이 들어오면 종료
    if n == 0: break

    # 도둑루피 현황
    m_ap = [list(map(int, input().split())) for _ in range(n)]
    # 루피를 최소로 먹기 위해 distance에 저장
    distance = [[INF] * n for _ in range(n)]
    q = []
    
    # 먹은 루피를 heap에 저장해서, 가장 적게 먹은 값부터 꺼내서 계산
    heapq.heappush(q, (m_ap[0][0], (0, 0)))
    distance[0][0] = m_ap[0][0]

    while q:
        dist, now = heapq.heappop(q)
        
        if now[0] == n - 1 and now[1] == n - 1: 
            print("Problem {0}: {1}".format(testcase, dist))
            break

        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]

            if x < 0 or y < 0 or x >= n or y >= n: continue
            
            cost = dist + m_ap[x][y]
            if distance[x][y] > cost:
                distance[x][y] = cost
                heapq.heappush(q, (cost, (x, y)))
    
    