from itertools import combinations
from bisect import bisect_left
def make_all_cases():
    languages = ['cpp', 'java', 'python', '-']
    works = ['backend', 'frontend', '-']
    experience = ['junior', 'senior', '-']
    soulfood = ['chicken', 'pizza', '-']

    cases = dict()

    for l in languages:
        for w in works:
            for e in experience:
                for s in soulfood:
                    cases[''.join([l, w, e, s])] = []
    return cases

def input_by_cases(details):
    for i in range(0, 5):
        for c in combinations([0, 1, 2, 3], i):
            temp = []
            for _ in range(0, 4):
                if _ in c:
                    temp.append('-')
                else:
                    temp.append(details[_])
            cases[''.join(temp)].append(int(details[4]))

def sort_cases():
    for c in cases:
        cases[c].sort()

cases = make_all_cases()

def solution(info, query):
    answer = []
    for i in info:
        details = i.split()
        input_by_cases(details)
    sort_cases()

    for q in query:
        details = q.split()
        target = int(details[-1])
        details = details[::2]
        print(''.join(details), cases[''.join(details)])
        if cases[''.join(details)] == []:
            answer.append(0)
        else:
            answer.append(len(cases[''.join(details)]) - bisect_left(cases[''.join(details)], target, lo=0, hi=len(cases[''.join(details)])))
    
    
    return answer
        

        
        


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))