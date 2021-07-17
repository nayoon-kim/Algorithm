import sys
input = sys.stdin.readline

n = int(input())

a, b = 1, 0
s = 0
if n == 1:
    s = a
for i in range(0, n - 1):
    s = a + b
    b = a
    a = s

print(s)