import sys
n = int(sys.stdin.readline())
user = dict()
correct = 0
wrong = 0
for _ in range(n):
    tmp = sys.stdin.readline().split()
    if tmp[1] == 'megalusion': continue

    if not tmp[1] in user:
        user[tmp[1]] = [0, 0]
        if int(tmp[2]) == 4:
            user[tmp[1]][0] += 1
        else:
            user[tmp[1]][1] += 1
    elif user[tmp[1]][0] != 1:
        if int(tmp[2]) == 4:
            user[tmp[1]][0] += 1
        else:
            user[tmp[1]][1] += 1
    

for u in user:
    if user[u][0] == 1:
        correct += user[u][0]
        wrong += user[u][1]

if (correct + wrong) == 0:
    print(0)
else:
    print(correct/(correct + wrong) * 100)