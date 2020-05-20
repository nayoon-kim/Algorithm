line = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

def solution(lines):
    answer=0
    time = []
    scope = []
    for l in lines:
        line = l.split(' ')
        time.append(line[1])
        scope.append(line[2].split('s')[0])

    for ti, sco in zip(time, scope):
        h, m, s = ti.split(':')

        for t in time:
            _h, _m, _s = t.split(':')

            if float(s) < float(_s) < float(s)+float(sco):








    return answer

print(solution(line))
