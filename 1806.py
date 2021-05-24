import sys
input = sys.stdin.readline

n, s = map(int, input().split())

a = list(map(int, input().split()))

cur = 0
snum = 0
si = 0
answer = n + 1
while cur < n:
    print("snum:", snum, "si:", si, "cur:", cur, "answer:", answer)
    if snum >= s or si >= n:
        if snum >= s:
            answer = min(answer, si - cur)
        snum -= a[cur]
        cur += 1
        continue

    snum += a[si]
    si += 1
if answer == n + 1:
    answer = 0
print(answer)