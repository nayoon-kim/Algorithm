
def start(route, tickets, _answer):
    if len(tickets) == 0:
        _answer.append(route.copy())
        return

    for index, ticket in enumerate(tickets):
        if route[-1] == ticket[0]:
            route.append(ticket[1])
            tickets.remove(ticket)
            start(route, tickets, _answer)
            tickets.insert(index, ticket)

def solution(tickets):
    answer = []
    _answer = []

    for index,ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            route = [ticket[0], ticket[1]]
            tickets.remove(ticket)
            start(route, tickets, _answer)
            tickets.insert(index, ticket)
    _answer.sort()
    answer = _answer[0]
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets3 = [["ICN", "SFO"], ["SFO","ICN"],["ICN","SFO"],["SFO","QRE"]]
print(solution(tickets3))
