
n = int(input())

h = 0
m = 0
s = 0

target = (n, 59, 59)
count = 0
while (h, m, s) != target:
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    
    s += 1

    if str(h).find('3') != -1 or str(m).find('3') != -1 or str(s).find('3') != -1:
        count += 1

print(count)