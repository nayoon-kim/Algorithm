import sys
n = int(sys.stdin.readline())
info = []
for _ in range(n):
    s, f = list(map(int, sys.stdin.readline().split()))
    info.append([f, s])

info = sorted(info)

tmp = info[0]
answer = []
answer.append(tmp)
for t in info[1:]:
    if tmp[0] <= t[1]:
        tmp = t
        answer.append(tmp)

print(len(answer))
