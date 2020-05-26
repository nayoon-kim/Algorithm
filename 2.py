def solution(n):
    answer = 0
    num = [1]
    three = 1
    while True:
        if len(num) > n:
            break
        three *= 3
        num.append(three)
        temp = num
        for i in range(0, len(temp) - 1):
            num.append(temp[i]+three)

    answer = num[n - 1]
    return answer

print(solution(16))
