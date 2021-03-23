from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    all_com = dict()

    for o in orders:
        o = list(o)
        o.sort()
        for i in range(2, len(o) + 1):
            order = list(map(join_tuple_string, list(combinations(o, i))))
            for _o in order:
                if _o in all_com:
                    all_com[_o] += 1
                else:
                    all_com[_o] = 1
    all_com = sorted(all_com.items(), key=(lambda x:x[1]), reverse=True)

    for c in course:
        temp = 2
        for o in all_com:
            if len(o[0]) == c and temp <= o[1]:
                temp = o[1]
                answer.append(o[0])
    answer.sort()
    return answer

# join tuple elements in a list
# 1. Initialize list with tuples that contain strings.
# 2. Write a function called join_tuple_string that takes a tuple as arguments and return a string
# 3. Join the tuples in the list using map(join_tuple_string, list) method.
# 4. Convert the result to list.
# 5. Print the result.

# Initializing the list with tuples
string_tuples = [('A', 'B', 'C')]

# function that converts tuple to string
def join_tuple_string(string_tuples) -> str:
    return ''.join(string_tuples)

# joining all the tuples
result = map(join_tuple_string, string_tuples)

# converting and printing the result
print(list(result))

# order1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course1 = [2, 3, 4]
# print(solution(order1, course1))

# order2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course2 = [2, 3, 5]
# print(solution(order2, course2))

# order3 = ["XYZ", "XWY", "WXA"]
# course3 = [2, 3, 4]
# print(solution(order3, course3))



# a new, empty counter
a = Counter()
# a new counter from an iterable
b = Counter('gallahad')
# a new counter from a mapping
c = Counter({'red': 4, 'blue': 2})
# a new counter from keyword args
d = Counter(cats=4, dogs=8)

print(sum(c.values()))
print(c)
c.clear()
print(c)

print(set(b))
print(dict(b))
print(b.items())
print(b.most_common())


c = Counter(a=3, b=1)
d = Counter(a=1, b=2, c=1)
print(c&d)
