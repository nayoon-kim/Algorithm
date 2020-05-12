# https://jay-ji.tistory.com/40?category=732905 참고
# 1. 문자를 n개 단위로 잘라서 비교하여 압축
# 2. 압축할 문자열을 n개 단위씩 증가하며 input과 비교
# 2-1. 동일한 문자열이 나오면 압축률 + 1
# 2-2. 새로운 문자열이 나오면 비교할 문자열 변경 후, "압축률+문자열"을 list에 저장
_str = ["andrunrunrun"]
for s in _str:
    min_num = len(s)
    min_str = ""

    # range를 1부터 시작했기 때문에 len(s)에서 1을 더해줘야 함 -> range(1, len(s) + 1)
    for i in range(1, len(s) + 1):
        output = ''
        str = s[0:i]
        cnt = 1 # 압축률

        # i개씩 증가
        for j in range(i, len(s) + 1, i):
            # 압축할 문자열과 같은 문자열이 나오는 경우 압축률 증가
            if str == s[j:j+i]:
                cnt += 1
            # 압축률과 압축문자열을 output에 추가 + 새로운 문자열 할당
            else:
                # output에 붙일 때는 zip_cnt가 1이상일 때에만 붙이는 것.
                output += "{}".format(cnt if cnt > 1 else '') + str
                # output += "{cnt}{str}".format(cnt=cnt if cnt>1 else '', str='('+str+')' if cnt > 1 else str)
                str = s[j:j+i]
                cnt = 1
        # 마지막 비교 문자열을 더해준다
        output += str
        # 최소 길이 update
        if min_num > len(output):
            min_num = len(output)
            min_str = output


    answer = min_num
    _answer = min_str
    print(answer)
    print(_answer)


# def compress(text, tok_len):
#     words = [text[i:i+tok_len]] for i in range(0, len(text), tok_len)
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     for a, b in zip(words, words[1:] + ['']):
#         if a==b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
# def solution(text):
#     return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
