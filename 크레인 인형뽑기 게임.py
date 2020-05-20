

def solution(board, moves):
    basket = []
    num = 0
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                basket.append(j[i-1])
                j[i-1] = 0
                break
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                del basket[-2:]
                num+=2
    return num





board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
