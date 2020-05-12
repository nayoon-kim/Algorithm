import queue
import copy
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def solution(board):
    answer = 0
    x = len(board)
    y = x
    temp = [[0] * x for i in range(0, y)]

    q = queue.Queue()
    temp[0][0] = 1
    q.put([0,0,0,temp, 'start'])
    min = 14400
    while q.empty() == False:
        cur = q.get()

        for i in range(0, x):
            print(cur[3][i])
        print(cur[2])
        print()
        for i in d:
            if cur[0] == x - 1 and cur[1] == x - 1:
                if min > cur[2]: min = cur[2]
            if cur[0]+i[0] > -1 and cur[0] + i[0] < x and cur[1] + i[1] > -1 and cur[1] + i[1] < y and cur[3][cur[0]+i[0]][cur[1]+i[1]] == 0:
                cur[3][cur[0]+i[0]][cur[1]+i[1]] = 1
                if board[cur[0]+i[0]][cur[1] + i[1]] == 0 and cur[2] < min:
                    if cur[4] == 'start':
                        if cur[0] == cur[0] + i[0]:
                            q.put([cur[0]+i[0], cur[1] + i[1], cur[2] + 100, copy.deepcopy(cur[3]), 'horizontal'])
                        elif cur[1] == cur[1] + i[1]:
                            q.put([cur[0]+i[0], cur[1] + i[1], cur[2] + 100, copy.deepcopy(cur[3]), 'vertical'])
                    if (cur[1] == cur[1] + i[1] and cur[4] == 'vertical') or (cur[0] == cur[0] + i[0] and cur[4] == 'horizontal'):
                        q.put([cur[0]+i[0], cur[1] + i[1], cur[2] + 100, copy.deepcopy(cur[3]), cur[4]])
                    elif (cur[1] == cur[1] + i[1] and cur[4] == 'horizontal'):
                        q.put([cur[0]+i[0], cur[1] + i[1], cur[2] + 600, copy.deepcopy(cur[3]), 'vertical'])
                    elif (cur[0] == cur[0] + i[0] and cur[4] == 'vertical'):
                        q.put([cur[0]+i[0], cur[1] + i[1], cur[2] + 600, copy.deepcopy(cur[3]), 'horizontal'])


    answer = min
    return answer

a = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
b = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(b))
