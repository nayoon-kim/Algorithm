import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
# count = 0

# while n != 1:

#     count += 1
#     if n % k == 0:
#         n = n // k
#         continue

#     n -= 1

# print(count)

result = 0

while True:
    # 한번 while문이 돌아갈 때 n이 k로 나눠질 수 있도록 숫자 세팅 + n을 k로 나누기 까지 진행.
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

    print(target, n)