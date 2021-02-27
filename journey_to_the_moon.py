import math
import os
import random
import re
import sys
from itertools import combinations
import math
import os
import random
import re
import sys
from itertools import combinations

def journeyToMoon(n, astronaut):
	# 같은 국가가 없는 경우 -1
    k = dict()
    for _ in range(0, n):
        k[_] = -1

    # 같은 국가가 있는 지 확인
    # 다음 작업을 하였을 때 나오는 결과물
    # k = {0: -1, 1: 0, 2: 0, 3: 0}
    for i, a in enumerate(astronaut):
        if k[a[0]] == -1 and k[a[1]] != -1:
            k[a[0]] = k[a[1]]
        elif k[a[0]] != -1 and k[a[1]] == -1:
            k[a[1]] = k[a[0]]
        elif k[a[0]] == -1 and k[a[1]] == -1:
            k[a[0]], k[a[1]] = i, i
        # 각각이 같은 국가가 있는데, 각각의 수가 다른 경우
        # 더 작은 수로 국가를 통일하기 위해서 하는 작업
        else:
            little_min = 0
            _min = 0
            if k[a[0]] > k[a[1]]:
                little_min = k[a[0]]
                _min = k[a[1]]
            else:
                little_min = k[a[1]]
                _min = k[a[0]]
   
            for i in range(n):
                if k[i] == little_min:
                    k[i] = _min
     
    # 다음 작업을 하였을 때 나오는 결과물
    # nation:  {-1: [0], 0: [1, 2, 3]}
    nation = dict()
    for _ in k:
        if not k[_] in nation:
            nation[k[_]] = list()
        nation[k[_]].append(_)
	
    # 국가번호만 추출(combinations 모듈을 사용하기 위해서 하는 작업)
    # 다음 작업을 하였을 때 나오는 결과물
    # nation_num:  [-1, 0]
    nation_num = list()    
    for n in nation:
        nation_num.append(n)

    # 국가간 나올 수 있는 조합 구하기
    # 다음 작업을 하였을 때 나오는 결과물
    # nation_combination:  [(-1, 0)]
    nation_combination = list(combinations(nation_num, 2))
   
   
    # 정답 구하기
    answer = 0
    
    for _ in nation_combination:
        answer += len(nation[_[0]]) * len(nation[_[1]])
	
    # nation[-1]에 속해있는 astronaut는 같은 국가가 아니기 때문에 각 astronaut을 다른 국가로 보고 nation[-1]의 조합을 구한다.
    if -1 in nation:
        answer += len(list(combinations(nation[-1], 2)))

    print(answer)
    # return answer
# def journeyToMoon(n, astronaut):
#     k = dict()
#     for _ in range(0, n):
#         k[_] = -1

#     for i, a in enumerate(astronaut):
#         if k[a[0]] == -1 and k[a[1]] != -1:
#             k[a[0]] = k[a[1]]
#         elif k[a[0]] != -1 and k[a[1]] == -1:
#             k[a[1]] = k[a[0]]
#         elif k[a[0]] == -1 and k[a[1]] == -1:
#             k[a[0]], k[a[1]] = i, i
#         else:
#             little_min = 0
#             _min = 0
#             if k[a[0]] > k[a[1]]:
#                 little_min = k[a[0]]
#                 _min = k[a[1]]
#             else:
#                 little_min = k[a[1]]
#                 _min = k[a[0]]
#             for i in range(n):
#                 if k[i] == little_min:
#                     k[i] = _min
#     print("k: ", k)
#     nation = dict()
    
#     for _ in k:
#         if not k[_] in nation:
#             nation[k[_]] = list()
#         nation[k[_]].append(_)

#     print("nation: ", nation)

#     nation_per = list()
    
#     for n in nation:
#         nation_per.append(n)

#     print("nation_per: ",nation_per)
#     kind_nation_per = list(combinations(nation_per, 2))
#     answer = 0
#     print("kind_nation_per: ", kind_nation_per)
#     for _ in kind_nation_per:
#         # print(nation[_[0]], nation[_[1]])
#         answer += len(nation[_[0]]) * len(nation[_[1]])

#     if -1 in nation:
#         answer += len(list(combinations(nation[-1], 2)))
#     # return answer
#     print(answer)
    
            
if __name__ == '__main__':

    # np = input().split()

    # n = int(np[0])

    # p = int(np[1])

    # astronaut = []

    # for _ in range(p):
    #     astronaut.append(list(map(int, input().rstrip().split())))

    # n = 10
    # p = 7
    # astronaut = [[0, 2], [1, 8], [1, 4], [2, 8], [2, 6], [3, 5], [6, 9]]
    # astronaut = [[0, 2]]

    n = 4
    p = 2
    astronaut = [[1, 2], [2, 3]]
    journeyToMoon(n, astronaut)
