import sys
input = sys.stdin.readline
n = int(input())
a, b, c, d = list(), list(), list(), list()

for i in range(n):
    t, e, m, p = map(int, input().split())
    a.append(t)
    b.append(e)
    c.append(m)
    d.append(p)

# a.sort()
# b.sort()
# c.sort()
# d.sort()
answer = list()
anum, bnum, cnum, dnum = 0, 0, 0, 0
while True:
    if dnum == n:
        cnum += 1
        dnum = 0
    if cnum == n:
        bnum += 1
        cnum = 0
    if bnum == n:
        anum += 1
        bnum = 0
    if anum == n:
        break
    
    if a[anum] + b[bnum] + c[cnum] + d[dnum] == 0:
        answer.append([anum, bnum, cnum, dnum])
    dnum += 1
 
print(len(answer))