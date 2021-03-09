from _operator import itemgetter

n, c = map(int, input().split())
info = []
status = []
m = int(input())

# 도착 지점이 작은 순으로 정렬
for i in range(m):
    x, y, z = map(int, input().split())
    info.append({'s': x, 'f': y, 'c': z})

info = sorted(info, key=itemgetter('f'))

sum = 0
total_sum = 0

for i in info:
    # 짐 내리기
    
    # 짐 싣기
    if sum >= c: continue
    if sum + i['c'] > c:
        i['c'] = c - sum
    status.append(i)

# for target in range(1, n + 1):
#     info[target] = sorted(info[target].items())

# for i in range(m):

# sum = 0
# total_sum = 0
# for target in range(1, n+1):
#     info[target] = sorted(info[target].items())
    
#     sum -= status[target]
#     total_sum += status[target]
#     status[target] = 0

#     # 짐 싣기
#     for t in info[target]:
#         _t0 = t[0]
#         _t1 = t[1]
        
#         if sum >= c: continue

#         if sum + _t1 > c:
#             _t1 = c - sum

#         status[_t0] += _t1
#         sum += _t1

# print(total_sum)
        
