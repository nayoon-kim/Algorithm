def solution(baseball):
    answer = 0


    for i in range(123, 988):
        s = str(i)
# 0이 들어갈 수 없고 서로 다른 1~9까지의 수로 이루어진 세자리 수
        if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            continue
        if s[0] == '0' or s[1] == '0' or s[2] == '0':
            continue
# 조건을 만족하지 않을 경우 flag를 False로 설정할 예정
        flag = True
# baseball에 있는 조건들을 통해서 조건 만족 시 answer의 값을 1 올려주고 아니면 그냥 넘어간다.
        for b_b in baseball:
            strike = 0
            ball = 0
            for a in range(3):
                for b in range(3):
                    _s = str(b_b[0])
                    # 숫자와 위치가 일치할 경우 strike는 1을 더해준다.
                    if a == b and s[a] == _s[b]:
                        strike+=1
                        continue
                    # 위치는 틀리고 숫자만 만족할 경우 ball은 1을 더해준다.
                    if a != b and s[a] == _s[b]:
                        ball+=1
                        continue
            # strike와 ball의 상태와 baseball의 조건을 비교해서 맞으면 flag=True, 틀리면 flag=False
            if strike != b_b[1] or ball != b_b[2]:
                flag = False
                break
        if flag == True:
            answer+=1

    return answer

baseball=[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))
