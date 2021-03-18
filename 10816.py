import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
gs = list(map(int, sys.stdin.readline().split()))

_s = list(set(s))
_s.sort()

s_dict = {}

for _ in _s:
    s_dict[_] = s.count(_)
    

def bsearch(n):
    low = 0
    high = len(_s) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if _s[mid] == n:
            return 1
        elif _s[mid] > n:
            high = mid - 1
        else:
            low = mid + 1
    return 0 

for g in gs:
    a = bsearch(g)
    answer = 0
    if a == 1:
        answer = s_dict[g]
    else:
        answer = 0
    print(answer, end=' ')