import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    a = 2 * m - n
    print(a, m - a)