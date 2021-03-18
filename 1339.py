import sys
alpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N':0, 'O': 0, 'P': 0, 'Q':0, 'R':0, 'X':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

num = int(sys.stdin.readline())
word_num = [sys.stdin.readline() for n in range(num)]
word_num_num = {}

total_num = 0
numbering = 9
for word in word_num:
    word_num_num[word] = len(word)
    total_num += len(word)

while True:
    res = sorted(word_num_num.items(), key=(lambda x: x[1]), reverse=True)
    print(res)
    if res[0][0] == '':
        total_num = 0

    if total_num == 0:
        break

    if  alpha[res[0][0][0]] != 0:
        word_num_num[res[0][0][1:]] = res[0][1] - 1
        del(word_num_num[res[0][0]])
        total_num -= 1
    else :
        alpha[res[0][0][0]] = numbering
    
        word_num_num[res[0][0][1:]] = res[0][1] - 1
        del(word_num_num[res[0][0]])    
        numbering -= 1
        total_num -= 1

real_num = []
for word in word_num:
    real = ''
    for w in word:
        real += str(alpha[w])
    real_num.append(int(real))

print(sum(real_num))
    


# # 다른 방식

t = int(input())

ss = []

for _ in range(t):
    ss.append(input())

alphabet = [0 for i in range(26)]

for s in ss:
    i = 0
    while s:
        now = s[-1]
        alphabet[ord(now) - ord('A')] += pow(10, i)
        i += 1
        s = s[:-1]
alphabet.sort(reverse=True)
print(alphabet)
ans = 0
for i in range(9, 0, -1):
    ans += i * alphabet[9-i]

print(ans)