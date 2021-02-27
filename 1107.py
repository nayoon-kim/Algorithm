from collections import deque
target = input()
n = list(target)
m = int(input())
if m != 0:
    f = list(map(int, input().split()))

d = [1, -1]

possibility = ['']
# 숫자 버튼을 누르는 경우
# 숫자 버튼을 누르지 않고 +, -만 누르는 경우
_min = len(n)
if m == 10:
    _min = int(target) - 100
elif m != 0:
    for i in n:
        if int(i) in f:
            q = deque([int(i)])
            count = 0
            check = [0] * 10
            tempo = possibility
            possibility = []
            while q:
                node = q.pop()
                check[node] = 1

                for _d in d:
                    if -1 < node + _d < 10:
                        if not node + _d in f:
                            for t in range(0, len(tempo)):
                                possibility.append(tempo[t]+str(node+_d))
                        else:
                            if check[node + _d] == 0:
                                q.append(node + _d)
                                print(node + _d)
            # for p in range(0, len(possibility)):
            #     possibility[p] += str(node+_d)
            
        else:
            for p in range(0, len(possibility)):
                possibility[p] += i

print(possibility)
temp_min = abs(int(target) - 100)
for p in possibility:
    if int(p) == 0: _min = 1
    temp = abs(int(p) - int(target))
    if temp_min > temp:
        temp_min = temp

_min += temp_min

print(_min)
