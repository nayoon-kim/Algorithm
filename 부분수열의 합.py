n, m = input().split()
# m = int(input())

a = input()
element = a.split(' ')
plus_num = 0
for i in range(0, len(element)):
    element[i] = int(element[i])

def backtracking(pos, sum):
    global plus_num
    if pos == len(element):
        return
    if sum + element[pos] == int(m): plus_num+=1

    backtracking(pos+1, sum)
    backtracking(pos+1, sum + element[pos])


backtracking(0, 0)
print(plus_num)
