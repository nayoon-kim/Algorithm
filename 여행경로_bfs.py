# 테스트 1 〉	통과 (1399.84ms, 27.9MB)
# 테스트 2 〉	통과 (0.09ms, 10.8MB)
# 테스트 3 〉	통과 (0.10ms, 10.8MB)
# 테스트 4 〉	통과 (0.10ms, 10.8MB)
# 진짜 가증스럽다..

import queue
def solution(tickets):
    answer = []
    visited = [0 for i in tickets]
    tickets.sort()
    q = queue.Queue()

    for index, ticket in enumerate(tickets):
        if ticket[0] =="ICN":
            v = visited.copy()
            v[index] = 1
            q.put([ticket, v, ticket])

    while q.empty() != True:
        t = q.get()
        # print(t)
        for index, ticket in enumerate(tickets):
            if t[0][1] == ticket[0] and t[1][index] != 1:
                _v = t[1].copy()
                _v[index] = 1
                _t = t[2].copy()
                _t.append(ticket[1])
                if len(_t) == len(tickets) + 1:
                    answer.append(_t)
                q.put([ticket, _v, _t])
    answer.sort()
    print(answer)
    del answer[1:]
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets3 = [["ICN", "SFO"], ["SFO","ICN"],["ICN","SFO"],["SFO","QRE"]]
print(solution(tickets2))
