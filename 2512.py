import sys

def result(n, lands, m):
    lands.sort()
    _max = lands[-1]
    _min = 0
    h = 0
    result = 0

    while _min <= _max:
        _sum = 0
        h = (_max + _min) // 2
        
        for land in lands:
            if land < h:
                _sum += land 
            else:
                _sum += h

        if _sum <= m:
            _min = h + 1
            result = h
        elif _sum > m: # _sum >= m
            _max = h - 1

    return result

def start():
    n = int(sys.stdin.readline())
    lands = list(map(int, sys.stdin.readline().split(' ')))
    m = int(sys.stdin.readline())

    print(result(n, lands, m))


start()