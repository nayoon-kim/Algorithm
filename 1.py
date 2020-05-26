def solution(p):
    answer = 0
    # while True:

    while True:
        p += 1
        a = [int(x) for x in str(p)]
        b = dict()

        for e in a:
            if e in b:
                b[e] += 1
            else:
                b[e] = 1

        if len(b) == len(a):
            break
    answer = p
    return answer

print(solution(1000))
