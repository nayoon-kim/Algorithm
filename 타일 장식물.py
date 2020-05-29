def solution(N):
    answer = 0
    arr = [0, 1]
    answer += (1 * 4)

    for i in range(N-1):
        arr.append(arr[i]+arr[i+1])
        answer += (arr[-1]*2)

    return answer

print(solution(5))
