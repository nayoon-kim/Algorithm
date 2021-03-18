import sys

user, rel = list(map(int, sys.stdin.readline().split()))
INF = 10000000
f = [[INF] * user for _ in range(user)]

for _ in range(rel):
    a, b = list(map(int, sys.stdin.readline().split()))
    f[a - 1][b - 1] = 1
    f[b - 1][a - 1] = 1

for _ in range(user):
    f[_][_] = 0

for k in range(user):
    for i in range(user):
        for j in range(user):
            if f[i][j] > f[i][k] + f[k][j]:
                f[i][j] = f[i][k] + f[k][j]
sum = INF
kevin = 0
for i, _ in enumerate(f):
    temp = 0
    for a in _:
        temp += a
    if temp < sum:
        sum = temp
        kevin = i + 1
    
print(kevin)