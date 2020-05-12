import re
import copy
a = "100-200*300-500+20"

def is_mul(expr):
    for i in expr:
        if i == '*':
            return True
    return False

def is_plus(expr):
    for i in expr:
        if i == '+':
            return True
    return False

def is_minus(expr):
    for i in expr:
        if i == '-':
            return True
    return False

def is_negative(expr):
    if int(expr) < 0:
        expr = str(int(expr)*-1)
    return expr

def multiply(expr):

    while is_mul(expr) == True:
        a = len(expr)
        for i in range(0, a):
            if expr[i] == "*":
                expr[i-1] = str(int(expr[i-1]) * int(expr[i+1]))
                del expr[i+1]
                del expr[i]
                break
    return expr

def plus(expr):
    while is_plus(expr) == True:
        a = len(expr)
        for i in range(0, a):
            if expr[i] == "+":
                expr[i-1] = str(int(expr[i-1]) + int(expr[i+1]))
                del expr[i+1]
                del expr[i]
                break
    return expr

def minus(expr):
    while is_minus(expr) == True:
        a = len(expr)
        for i in range(0, a):
            if expr[i] == "-":
                expr[i-1] = str(int(expr[i-1]) - int(expr[i+1]))
                del expr[i+1]
                del expr[i]
                break
    return expr

def solution(expression):
    answer = 0
    splitted = re.split(r"[\+\-\*]", expression)
    min = 1
    operator_set = []
    list1 = []
    for i in a:
        if i == '-':
            splitted.insert(min, i)
            min+=2
            operator_set.append(i)
        elif i == '+':
            splitted.insert(min, i)
            min+=2
            operator_set.append(i)
        elif i == '*':
            splitted.insert(min, i)
            min+=2
            operator_set.append(i)

    operator_set = list(set(operator_set))
    if len(operator_set) == 1:
        if operator_set[0] == '+':
            list1.append(plus(splitted))
        elif operator_set[0] == '*':
            list1.append(multiply(splitted))
        elif operator_set[0] == '-':
            list1.append(minus(splitted))
    elif len(operator_set) == 2:
        str = ''
        splitted1 = copy.deepcopy(splitted)
        splitted2 = copy.deepcopy(splitted)
        for i in operator_set:
            str+=i
        if str == '+-' or str == '-+':
            list1.append(plus(minus(splitted1)))
            list1.append(minus(plus(splitted2)))
        elif str == '*-' or str == '-*':
            list1.append(multiply(minus(splitted1)))
            list1.append(minus(multiply(splitted2)))
        elif str == '+*' or str == '*+':
            list1.append(multiply(plus(splitted1)))
            list1.append(plus(multiply(splitted2)))
    elif len(operator_set) == 3:
        splitted1 = copy.deepcopy(splitted)
        splitted2 = copy.deepcopy(splitted)
        splitted3 = copy.deepcopy(splitted)
        splitted4 = copy.deepcopy(splitted)
        splitted5 = copy.deepcopy(splitted)
        splitted6 = copy.deepcopy(splitted)

        list1.append(multiply(plus(minus(splitted1))))
        list1.append(multiply(minus(plus(splitted2))))
        list1.append(plus(minus(multiply(splitted3))))
        list1.append(plus(multiply(minus(splitted4))))
        list1.append(minus(plus(multiply(splitted5))))
        list1.append(minus(multiply(plus(splitted6))))

    for i in list1:
        for t in i:
            temp = is_negative(t)
            if answer < int(temp):
                answer = int(temp)

    return answer
