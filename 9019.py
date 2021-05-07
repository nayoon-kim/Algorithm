import sys
from collections import deque
input = sys.stdin.readline

def digit_length(n):
    ans = 0
    answer = []
    while n:
        answer.append(n%10)
        n //= 10
        ans += 1
    
    return ans, answer

# result = 1234
# num, e_num = digit_length(result)

# L = result - 10 ** (num - 1) * e_num[-1]
# print(L)
# L = L * 10+ e_num[-1]
# print(L)

# R = result // 10 + e_num[0] * 10 ** (num - 1)
# print(R)
testcase = int(input())
for _ in range(testcase):
    a, b = map(int, input().split())
    c = [0 for _ in range(10000)]
    q = deque()
    q.append([a, ''])
    c[a] = 1

    while q:
        result, results = q.popleft()
        
        if result == b:
            print(results)
            break
        # D
        D = result * 2
        if D > 9999:
            D %= 10000
        if c[D] == 0:
            c[D] = 1
            q.append([D, results + 'D'])
        
        # S
        S = result - 1
        if result == 0:
            S = 9999
        if c[S] == 0:
            c[S] = 1
            q.append([S, results + 'S'])

        # L
        L = (result % 1000) * 10 + (result // 1000)
        # print("L:", L)  
        if c[L] == 0:
            c[L] = 1
            q.append([L, results + 'L'])

        # R
        R = (result % 10) * 1000 + (result // 10)
        # print("R:", R)
        if c[R] == 0:
            c[R] = 1
            q.append([R, results + 'R'])