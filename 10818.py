import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
INF = 1000001
ma, mi = -1 * INF, INF

for i in l:
    if i < mi:
        mi = i
    if i > ma:
        ma = i

print(mi, ma)