origin = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:16, 11: 4}
def percentage(sum, card):
    limited = 21 - sum
    if limited < 0 :
        return "STOP"
    if limited > 11:
        return "GAZUA"
    winning_num = 0
    losing_num = 0
    card[11] = card[1]
    for i in range(2, limited + 1):
        winning_num += card[i]
    for i in range(limited+1, 12):
        losing_num += card[i]

    if losing_num > winning_num:
        return "STOP"
    return "GAZUA"

testcase = int(input())
for i in range(0, testcase):
    sub_testcase = int(input())
    card = origin
    sum = 0
    for j in range(0, sub_testcase):
        n = int(input())
        sum+=n
        card[n] -= 1
    print("#{"+str(i)+"} "+str(percentage(sum, card)))
