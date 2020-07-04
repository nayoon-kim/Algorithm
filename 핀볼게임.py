# ↑ = 0, ↓ = 1, → = 2, ← = 3
def solution(arr, num, index, _index, dir):
    i, j, d = index, _index, dir
    visited = 0
    while True:

        if d == 0:
            if i < 0:
                d = 1
                num += 1
                i += 1
                continue

            if arr[i][j] == 1 or arr[i][j] == 4 or arr[i][j] == 5:
                d = 1
            elif arr[i][j] == 2:
                d = 2
            elif arr[i][j] == 3:
                d = 3
            elif arr[i][j] == 0:
                if i == index and j == _index and visited != 0:
                    break
                visited += 1
                d = 0
                i -= 1
                print("value: 0, d == 0, {0},{1}".format(i, j))
                continue
            else:
                for _a, a in enumerate(arr):
                    for _b, b in enumerate(a):
                        if arr[i][j] == b and (i != _a or j != _b):
                            i, j = _a, _b
                            break
                continue
            print("d == 0, {0},{1}".format(i, j))
        elif d == 1:
            if i > len(arr) - 1:
                d = 0
                num += 1
                i -= 1
                continue

            if arr[i][j] == 2 or arr[i][j] == 3 or arr[i][j] == 5:
                d = 0
            elif arr[i][j] == 0:
                if i == index and j == _index and visited != 0:
                    break
                visited += 1
                d = 1
                i += 1
                print("value: 0, d == 1, {0},{1}".format(i, j))
                continue
            elif arr[i][j] == 1:
                d = 2
            elif arr[i][j] == 4:
                d = 3
            else:
                for _a, a in enumerate(arr):
                    for _b, b in enumerate(a):
                        if arr[i][j] == b and (i != _a or j != _b):
                            i, j = _a, _b
                            break
                continue
            print("d == 1, {0},{1}".format(i, j))
        elif d == 2:
            if j > len(arr) - 1:
                d = 3
                num += 1
                j -= 1
                continue

            if arr[i][j] == 1 or arr[i][j] == 2 or arr[i][j] == 5:
                d = 3
            elif arr[i][j] == 0:
                if i == index and j == _index and visited != 0:
                    break
                visited += 1
                d = 2
                j += 1
                print("value: 0, d == 2, {0},{1}".format(i, j))
                continue
            elif arr[i][j] == 3:
                d = 1
            elif arr[i][j] == 4:
                d = 0
            else:
                for _a, a in enumerate(arr):
                    for _b, b in enumerate(a):
                        if arr[i][j] == b and (i != _a or j != _b):
                            i, j = _a, _b
                            break
                continue
            print("d == 2, {0},{1}".format(i, j))
        elif d == 3:
            if j < 0:
                d = 2
                num += 1
                j += 1
                continue

            if arr[i][j] == 3 or arr[i][j] == 4 or arr[i][j] == 5:
                d = 2
            elif arr[i][j] == 0:
                if i == index and j == _index and visited != 0:
                    break
                visited += 1
                d = 3
                j -= 1
                print("value: 0, d == 3, {0},{1}".format(i, j))
                continue
            elif arr[i][j] == 1:
                d = 0
            elif arr[i][j] == 2:
                d = 1
            else:
                for _a, a in enumerate(arr):
                    for _b, b in enumerate(a):
                        if arr[i][j] == b and (i != _a or j != _b):
                            i, j = _a, _b
                            break
                continue
            print("d == 3, {0},{1}".format(i, j))
        if d == 0:
            i -= 1
        elif d == 1:
            i += 1
        elif d == 2:
            j += 1
        else:
            j -= 1

        num += 1

        if arr[i][j] == -1:
            break
    print(num)

# # ↑ = 0, ↓ = 1, → = 2, ← = 3
# 1 ->
# 위 : 아래, 아래 : 오른쪽, 왼쪽 : 위쪽, 오른쪽
# →: ←, ←: ↑, ↓: →, ↑: ↓
# 2: 3, 3: 0, 1: 2, 0: 1
#
# 2 ->
# →: ←, ↓: ↑, ←:↓, ↑:→
# 2: 3, 1:0, 3: 1, 0:2
# 3->
# →: ↓, ↓: ↑, ←:→, ↑:←
# 2:1, 1:0, 3:2, 0:3
# 4->
# ↑: ↓, ←: →, ↓:←, →:↑
# 0:1, 3:2, 1:3, 2:0
# 5->
# →: ←, ↓: ↑, ↑: ↓, ←: →
# 2:3, 1:0, 0:1, 3:2

# 벽에 즉각적으로 튕겨나온 핀볼에 대한 처리가 없음
# 벽에 즉각적으로 튕겨나온 핀볼에 대한 처리가 없음
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    num = 0
    for index, i in enumerate(arr):
        for _index, j in enumerate(i):
            if arr[index][_index] == 0:
                for dir in range(0, 4):
                    print("{0},{1},{2} go in".format(index, _index, dir))
                    solution(arr, num, index, _index, dir)
    print("#{0} {1}".format(test_case, num))

"""
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
"""
