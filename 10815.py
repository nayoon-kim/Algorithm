import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
gs = list(map(int, sys.stdin.readline().split()))

# 이분탐색은 데이터가 정렬되어 있어야한다.
s.sort()

def bsearch(n):
    low = 0
    high = len(s) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        
        if s[mid] == n:
            return 1
        elif s[mid] > n:
            high = mid - 1
        else:
            low = mid + 1
    return 0

answer = []
for i in gs:
    answer.append(bsearch(i))

for i in answer:
    print(i, end=' ')
