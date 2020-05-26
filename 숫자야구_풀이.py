
import itertools

def st_B(given, chosen):
    st = 0
    B = 0
    chosen_dif = []
    given_dif = []
    for i in range(3):
        if given[i] == chosen[i]:
            st += 1
        else:
            given_dif.append(given[i])
            chosen_dif.append(chosen[i])
    for num in chosen_dif:
        if num in given_dif:
            B += 1
    return st, B

def solution(baseball):
    # 순열 출력
    first = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
    second = []
    for each in baseball:
        given = [int(i) for i in str(each[0])]
        stb = (each[1], each[2])
        for chosen in first:
            if st_B(given, chosen) == stb:
                second.append(chosen)
        first = second
        second = []
    return len(first)
baseball=[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))
