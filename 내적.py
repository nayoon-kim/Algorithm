# 월간 코드 챌린지 1회

def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    return answer
