import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

cur = 0
s = 0
si = cur
answer = 0
while cur < n:
    print("s:", s, "si:", si, "cur:", cur, "answer:", answer)
    if s >= m or si >= n:
        if s == m:
            answer += 1
        cur += 1
        s = 0
        si = cur
        continue

    s += a[si]
    si += 1

print(answer)
    