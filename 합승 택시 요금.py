def solution(n, s, a, b, fares):
    answer = 0
    INF = 987654321
    dest = [[INF] * (n+1) for _ in range(n+1)]
    
    for f in fares:
        dest[f[0]][f[1]] = f[2]
        dest[f[1]][f[0]] = f[2]

    for i in range(1, n+1):
        dest[i][i] = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dest[i][j] > dest[i][k] + dest[k][j]:
                    dest[i][j] = dest[i][k] + dest[k][j]
    print(dest)
    result = []
    # 둘이 따로 가는 방법
    each_fares = dest[s][a] + dest[s][b]
    result.append(each_fares)

    # 둘이 같이 가는 방법
    for i in range(1, n+1):
        if i == s: continue
        result.append(dest[s][i] + dest[i][a] + dest[i][b])
    
    answer = min(result)
    return answer

# a= solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])

n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n, s, a, b, fares))
# print(a)