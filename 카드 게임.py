def solution(left, right):
    answer = 0
    dp = [[0 for i in range(len(left)+1)] for _ in range(len(right)+1)]
    for i in reversed(range(len(right))):
        for j in reversed(range(len(left))):
            if left[j] > right[i]:
                dp[i][j] = dp[i+1][j] + right[i]
            else:
                dp[i][j] - max(dp[i+1][j+1], dp[i][j+1])
    answer = dp[0][0]
    return answer

# 반복문을 이용해서 푸는 방식은 0번째 부터 DP 배열을 채우는 게 아니라,
# N-1번째부터 역방향으로 채우면 된다.

left = [2, 1, 1]
right = [3, 1, 1]
print(solution(left, right))
