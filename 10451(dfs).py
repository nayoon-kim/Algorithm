import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다.
input = sys.stdin.readline
testcase = int(input())

def dfs(x):
    visited[x] = True
    cycle = cycle_input[x]
    if not visited[cycle]:
        dfs(cycle)

for _ in range(testcase):
    n = int(input())
    cycle_input = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n #방문여부 확인
    result = 0

    for i in range(1, n + 1):
        if not visited[i]: #방문하지 않았다면
            dfs(i) #dfs 실행
            result += 1 #결괏값 += 1
    print(result)