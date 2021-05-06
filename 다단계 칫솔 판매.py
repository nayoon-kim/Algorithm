def solution(enroll, referral, seller, amount):
    answer = []
    _enroll = {}
    result = {}
    result["-"] = 0
    for e, r in zip(enroll, referral):
        _enroll[e] = r
        result[e] = 0
    for s, a in zip(seller, amount):
        a_mount = a * 100
        sell_er = s
        result[sell_er] += a_mount
        while True:
            a_mount = a_mount // 10
            if a_mount < 1:
                break
            else:
                result[sell_er] -= a_mount
                result[_enroll[sell_er]] += a_mount
                sell_er = _enroll[sell_er]
            if sell_er == "-":
                break
            
    for r in result:
        answer.append(result[r])
    answer = answer[1:]
    return answer