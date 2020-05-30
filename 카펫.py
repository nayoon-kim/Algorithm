def solution(brown, yellow):
    answer = []
    total=brown+yellow
    for n in range(2, total):
        t = int(total / n)
        if total % n == 0 and (t - 2)*(n - 2) == yellow:
            answer.append(t)
            answer.append(n)
            break
    return answer

brown=10
yellow=2
print(solution(brown, yellow))
