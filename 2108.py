import sys
input = sys.stdin.readline

n = int(input())

q = list()
p = [0] * 8002

for i in range(n):
    a = int(input())
    q.append(a)
    p[a + 4000] += 1

avg = round(sum(q) / n)

q.sort()

mid = q[n//2]

ma_x = max(p)
ma_x_list = list()

for i in range(0, 8002):
    if ma_x == p[i]:
        ma_x_list.append(i-4000)

# 산술평균
print(avg)

# 중앙값
print(mid)

# 최빈값
many = ma_x_list[0]
if len(ma_x_list) > 1:
    many = ma_x_list[1]
print(many)

# 범위
ran = max(q) - min(q)
print(ran)
