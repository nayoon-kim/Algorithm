from itertools import combinations
import sys

n = int(sys.stdin.readline())
person = list()
for _ in range(n):
    person.append(_)
skills = [list(map(int, sys.stdin.readline().split())) for i in range(n)]


combination = list(combinations(person, n//2))
print(combination)