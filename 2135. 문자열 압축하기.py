str = ["letsgogogoletsgogogo"]

for s in str:
    min_num = len(s)
    min_str = ""
    for j in range(1, len(s)+1):
        output = ''
        _s = s[0:j]
        cnt = 1
        for k in range(j, len(s)+1, j):

            if _s == s[k:k+j]:
                cnt+=1
            else:
                output += "{cnt}{str}".format(cnt=cnt if cnt>1 else '', str='('+_s+')' if cnt > 1 else _s)
                _s = s[k:k+j]
                cnt = 1
        output += _s

        if min_num > len(output):
            min_num = len(output)
            min_str = output

    print(min_num)
    print(min_str)
