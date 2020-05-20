# import queue
# def solution(n):
#     answer = []
#     answer.append(0)
#
#     while n != 1:
#         _answer = []
#         for index, value in enumerate(answer):
#             if index % 2 == 0:
#                 if value == 0:
#                     _answer.extend([0, 0, 1])
#                 else:
#                     _answer.extend([0, 1, 1])
#             else:
#                 _answer.append(value)
#         n-=1
#         answer = _answer
#     return answer

def solution(n):
    fold = 0
    arr = [fold]

    for i in range(n - 1):
        arr = arr + [fold] + [bit ^ 1 for bit in arr[::-1]]

    return arr

n = 2
print(solution(4))
