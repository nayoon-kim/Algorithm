import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list()

cur = 0
an = 0
bn = 0
rn = 0
while True:
    if an >= n:
        c.extend(b[bn:])
        break
    if bn >= m:
        c.extend(a[an:])
        break
    
    if a[an] < b[bn]:
        c.append(a[an])
        an += 1
    else:
        c.append(b[bn])
        bn += 1
    cur += 1

for i in c:
    print(i, end=' ')