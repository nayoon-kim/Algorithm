# from itertools import combinations
# def solution(clothes):
#     answer = 0
#     cloth = dict()
#     for c in clothes:
#         if not c[1] in cloth:
#             cloth[c[1]] = 1
#         else:
#             cloth[c[1]] += 1
#     items = list(range(len(cloth)))
#     values = list()
#     for c in cloth:
#         values.append(cloth[c])
#
#     for n in range(1, len(cloth)+1):
#         num = list(combinations(items, n))
#         for i in num:
#             if len(i) > 1:
#                 sum = 1
#                 for j in i:
#                     sum *= values[j]
#                 answer += sum
#             else:
#                 answer += values[i[0]]
#
#     return answer

# def solution(clothes):
#     answer = 1
#     cloth = dict()
#     for c in clothes:
#         if not c[1] in cloth:
#             cloth[c[1]] = 1
#         else:
#             cloth[c[1]] += 1
#     for num in cloth.values():
#         answer *= (num+1)
#     # values = list()
#     # for c in cloth:
#     #     values.append(cloth[c])
#     # print(values)
#     # for v in values:
#     #     answer *= (v+1)
#     answer -= 1
#     return answer

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x *(y+1), cnt.values(), 1) - 1
    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes1 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
