n = int(input())

_min = 5000

for i in range(0, int(n/5)+1):
    t = n
    t -= 5 * i
    temp = -1
    if t % 3 == 0:
        temp = int(t / 3) + i
    if _min > temp and temp != -1:
        _min = temp


print(_min) if _min != 5000 else print(-1)