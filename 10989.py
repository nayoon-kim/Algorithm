import sys
input = sys.stdin.readline

n = int(input())

# 10,000보다 작거나 같은 자연수
q = [0] * 10001

for i in range(n):
    q[int(input())] += 1

for i in range(1, 10001):
    if q[i] != 0:
        for j in range(q[i]):
            print(i)