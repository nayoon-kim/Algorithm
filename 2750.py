import sys
input = sys.stdin.readline

n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))

l.sort()
for i in l:
    print(i)