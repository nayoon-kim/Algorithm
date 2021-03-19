a, p = map(int, input().split())

d = list()
d.append(a)
tmp = 0
while True:
    k = 0
    t = d[-1]
    while t != 0:
        k += (t % 10) ** p
        t //= 10
        
    d.append(k)
    # print(len(set(d)), len(d))
    if len(set(d)) != len(d):
        tmp = k
        break

idx = d.index(tmp)
print(len(d[:idx]))

    