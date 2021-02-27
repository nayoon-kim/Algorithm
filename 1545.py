def findKthBit(n: int, k: int) -> str:
    s = ["0"]
        
    for i in range(1, n + 1):
        temp = s[i-1].replace('0','-').replace('1', '0').replace('-', '1')
        s.append(s[i-1] + "1" + temp[::-1])
    print(s)
    return s[n][k-1]

print(findKthBit(1, 1))