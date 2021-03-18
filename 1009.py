import sys

n = int(sys.stdin.readline())
a = []
b = []

for i in range(n):
    tmp1, tmp2 = list(map(int, sys.stdin.readline().split()))
    a.append(tmp1)
    b.append(tmp2)

ab = dict()

def end_num(num):
    answer = []
    start = 1
    while True:
        start *= num
        tmp = int(str(start)[-1])
        if tmp in answer:
            break
        answer.append(tmp)
    return answer

answer = []
for _a, _b in zip(a, b):
    k = end_num(_a)
    if k[(_b % len(k))-1] == 0:
        answer.append(10)
    else:
        answer.append(k[(_b % len(k))-1])
    
print(answer)
