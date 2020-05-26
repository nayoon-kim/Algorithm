user_input = list(map(int, input().split()))
table = []
op = []
for i in range(user_input[0]):
	table.append(list(map(int, input().split())))
for i in range(user_input[2]):
	op.append(list(map(int, input().split())))

def solution(user_input, table, op):
	for o in op:
		start = [o[0], o[1]]
		finish = [o[2], o[3]]
		corner_up = table[o[0]][o[1]]
		corner_down = 0
		for i in range(o[1], o[3]):
			corner_down = table[o[0]][i+1]
			table[o[0]][i + 1] = corner_up
			corner_up = corner_down

        for j in range(o[0], o[2]):
            corner_down = table[j+1][o[3]]
            table[j+1][o[3]] = corner_up
            corner_up = corner_down

        for i in range(o[3], o[1]):
            corner_down = table[o[2]][i-1]
            table[o[2]][i-1]=corner_up
            corner_up = corner_down

        for i in range(o[2], o[0]):
            corner_down = table[i-1][o[1]]
            table[i-1][o[1]] =corner_up
            corner_up=corner_down

    	print(table)


user_input = [3, 4, 2]
table=[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
op=[[1, 1, 3, 4],[1, 3, 3, 4]]

solution(user_input, table, op)
