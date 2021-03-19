import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())

ele = list(map(int, sys.stdin.readline().rstrip().split()))

ele.sort(reverse=True)

sum = 0
_k = k
for _ in range(m):
    if _k == 0:
        _k = k
        sum += ele[1]
    else:
        sum += ele[0]
        _k -= 1
    

print(sum)