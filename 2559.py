import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = 0
cur = 0
answer = -(int(1e9))
temp = 0
while end < n:
    temp += a[end]
    end += 1
    cur += 1

    if cur == k:
        answer = max(answer, temp)
        temp -= a[start]
        start += 1
        cur -= 1

print(answer)