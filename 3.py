import queue
def solution(total_sp, skills):
    answer = []
    a = dict()
    for s in skills:
        a[s[0]] = []
        a[s[1]] = []

    for s in skills:
        a[s[0]].append(s[1])

    k = dict()
    for i in a:
        if a[i] == []:
            k[i] = 1
    n = 2
    while True:
        for i in a:
            temp = 0
            if not i in k:
                for j in a[i]:
                    if j in k:
                        temp += k[j]
                    else:
                        temp = -1
                        break
                if temp != -1:
                    k[i] = temp

        if len(k) == len(a):
            break
    num = 0
    max_num = 0
    root = 0
    for i in k:
        num += k[i]
        if k[i] > max_num :
            max_num = k[i]
            root = i

    num = int(total_sp / num)

    q = queue.Queue()
    q.put(root)

    for i in a:
        r = q.get()
        answer.append(k[r]*num)
        for i in a[r]:
            q.put(i)

    return answer

total_sp = 121
skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
print(solution(total_sp, skills))
