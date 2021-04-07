import sys
from itertools import combinations

n = int(sys.stdin.readline())

chu = [1, 3, 7, 26, 94, 259]

if n in chu:
    print(str(n) +' 0 ' + str(n))
    sys.exit(0)

answers = []
# 분리
for i in range(1, len(chu) + 1):
    answers.append(list(combinations(chu, i)))

for answer in answers:
    for a in answer:
        if n == sum(a):
            print(n + ' 0 ' + ' '.join(a))
            sys.exit(0)

# 분리 X
for answer in answers:
    for i in range(1, len(answer) + 1):
        expected = list(combinations(answer, i))
        for e in expected:
            if n + 