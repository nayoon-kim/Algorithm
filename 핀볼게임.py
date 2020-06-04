# ↑ = 0, ↓ = 1, → = 2, ← = 3
def solution(arr, num, index, _index, dir):
    i, j, d = index, _index, dir

    while True:
        if i < 0:

        elif i > len(arr) - 1:
        elif j < 0:
        elif j > len(arr) - 1:

        if arr[i][j] == -1 or (i == index and j == _index):
            print(num)
            break
        if arr[i][j] == 0:
            if d == 0:
                i += 1
            elif d == 1:
                i -= 1
            elif d == 2:
                j += 1
            else:
                j -= 1
            continue
        elif arr[i][j] == 1:
            if d == 0:
                d = 1
            elif d == 1:
                d = 2
            elif d == 2:
                d == 3
            elif d == 3:
                d = 0
        elif arr[i][j] == 2:
            if d == 0:
                d = 2
            elif d == 1:
                d = 0
            elif d == 2:
                d == 3
            elif d == 3:
                d = 1
        elif arr[i][j] == 3:
            if d == 0:
                d = 3
            elif d == 1:
                d = 0
            elif d == 2:
                d == 1
            elif d == 3:
                d = 2
        elif arr[i][j] == 4:
            if d == 0:
                d = 1
            elif d == 1:
                d = 3
            elif d == 2:
                d == 0
            elif d == 3:
                d = 2
        elif arr[i][j] == 5:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d == 3
            elif d == 3:
                d = 2
        else:
            for _a, a in enumerate(arr):
                for _b, b in enumerate(a):
                    if arr[i][j] == b and (i != _a or j != _b):
                        i, j = _a, _b
                        break
            continue

        if d == 0:
            i += 1
        elif d == 1:
            i -= 1
        elif d == 2:
            j += 1
        else:
            j -= 1

        num += 1

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    num = 0
    for index, i in enumerate(arr):
        for _index, j in enumerate(i):
            for dir in range(0, 4):
                solution(arr, num, index, _index, dir)
    print("#{0} {1}".format(test_case, num))

# 1
# 10
# 0 1 0 3 0 0 0 0 7 0
# 0 0 0 0 -1 0 5 0 0 0
# 0 4 0 0 0 3 0 0 2 2
# 1 0 0 0 1 0 0 3 0 0
# 0 0 3 0 0 0 0 0 6 0
# 3 0 0 0 2 0 0 1 0 0
# 0 0 0 0 0 1 0 0 4 0
# 0 5 0 4 1 0 7 0 0 5
# 0 0 0 0 0 1 0 0 0 0
# 2 0 6 0 0 4 0 0 0 4
