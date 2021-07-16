import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = 0
answer = 0

for i in range(1, n+1):
    if n % i == 0:
        c += 1
        if c == k:
            answer = i
            break

print(answer)
   