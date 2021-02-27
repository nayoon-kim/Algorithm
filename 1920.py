import sys

def binary_search(n, nlist, m, mlist):
    nlist.sort()

    for ml in mlist:
        _min = 0
        _max = n
        answer = 0
        while _min <= _max:
            h = (_max + _min) // 2
            
            if ml < nlist[h]:
                _max = h - 1
            elif ml > nlist[h]:
                _min = h + 1
            else:
                answer = 1
                break
        print(answer)
 
def start():
    n = int(sys.stdin.readline())
    nlist = list(map(int, sys.stdin.readline().split(' ')))
    m = int(sys.stdin.readline())
    mlist = list(map(int, sys.stdin.readline().split(' ')))
    binary_search(n, nlist, m, mlist)
start()