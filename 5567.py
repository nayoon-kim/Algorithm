import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
rel = dict()
invited = [False] * (n + 1)
for i in range(1, n + 1):
    rel[i] = []
for _ in range(m):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

invited[1] = True
for i in rel[1]:
    invited[i] = True
answer = []
for i in range(2, n + 1):
    if invited[i]:
        answer.extend(rel[i])

answer = list(set(answer))

for i in answer:
    invited[i] = True

print(invited.count(True) - 1)
            