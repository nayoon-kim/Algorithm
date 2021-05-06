
def solution(rows, columns, queries):
    answer = []
    square = []

    # make square
    for i in range(1, rows + 1):
        temp = []
        for j in range(1, columns + 1):
            temp.append(j + (i - 1) * rows)
        square.append(temp)

    for query in queries:
        
        a, b, c, d = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        
        temp1 = square[a][b]
        minimum = temp1
            
        # top to down
        for i in range(a, c):
            temp = square[i + 1][b]
            square[i][b] = temp
            minimum = min(temp, minimum)
            
         # left to right
        for i in range(b, d):
            temp = square[c][i + 1]
            square[c][i] = temp
            minimum = min(temp, minimum)
           
        # down to top
        for i in range(c, a, -1):
            temp = square[i - 1][d]
            square[i][d] = temp
            minimum = min(temp, minimum)
            
        # right to left
        for i in range(d, b, -1):
            temp = square[a][i - 1]
            square[a][i] = temp
            minimum = min(temp, minimum)
            
        square[a][b + 1] = temp1
        answer.append(minimum)

    return answer