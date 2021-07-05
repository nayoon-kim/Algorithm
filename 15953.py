import sys
input = sys.stdin.readline

code2017 = {1: 500, 2: 300, 3: 200, 4: 50, 5: 30, 6: 10}
code2018 = {1: 512, 2: 256, 3: 128, 4: 64, 5: 32}
UNIT = 10 ** 4

def code2017_m(a):
    if a == 0 or a > 21:
        return 0
    
    cur = 0
    for i in range(1, 7):
        cur += i
        if a <= cur:
            return code2017[i] * UNIT
    
    
def code2018_m(b):
    if b == 0 or b > 31:
        return 0
    
    cur = 0
    for i in range(1, 6):
        cur += 2 ** (i-1)
        if b <= cur:
            return code2018[i] * UNIT


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(code2017_m(a) + code2018_m(b))

    
