testcase = []

while True:
    _input = list(map(int, input().split()))
    if _input == [0, 0, 0]:
        break
    testcase.append(_input)

for i, t in enumerate(testcase):
    l, p, v = t
    temp1 = int(v / p)
    temp2 = int(v % p)
    result = temp1 * l
    result += temp2 if temp2 < l else l
    print("Case ", i+1, ": ", result, sep='')