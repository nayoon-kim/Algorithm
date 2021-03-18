n = int(input())
chu = list(map(int, input().split()))
chu = sorted(chu)
s = sum(chu)
answer = s - chu[-1] + 1
print(answer)