# def countSubstrings(s, t):

#     sum = 0
#     for i in range(1, len(s)+1):
#         for j in range(0, len(s)-i):
#             sum += compareString(s[j:j+i], t, i)
#     print(sum)


# def compareString(s, t, l):
#     _t = 0
#     sum = 0
#     while True:
#         if _t == len(t) - l:
#             break
#         temp = t[_t: _t + l]
#         num = 0
#         for i, _s in enumerate(s):
#             if temp[i] == _s:
#                 num += 1
#         if num == 1:
#             sum += 1
#     return sum


# countSubstrings("aba","baba")

import math

def majorityElement(nums):
    num = math.floor(len(nums)/2)
    
    nums_dict = dict()
    result = 0
    for i in nums:
        if not i in nums_dict:
            nums_dict[i] = 1
        else:
            nums_dict[i] += 1
        
    for n in nums_dict:
       if nums_dict[n] >= num:
           num = nums_dict[n]
           result = n

    return result


majorityElement([2,2,1,1,1,2,2])


from collections import Counter

num = math.floor(len(nums)/2)
a = Counter([2,2,1,1,1,2,2])

result = 0
for i in a:
    if a[i] >= num:
        num = a[i]
        result = i
print(result)