# https://jay-ji.tistory.com/41?category=732905
# temp = [[0] * key_size for i in range(0, key_size)]
# if key_size == 3
# print(temp) -> [[0,0,0],[0,0,0],[0,0,0]]
# 90도 lotate -> 3x3 기준 [0][*] => [*][2], [1][*] => [*][1], [2][*] =>[*][0]
def lotate(_key):
    key_size = len(_key)
    temp_key = [[0] * key_size for i in range(0, key_size)]

    reverse_i = key_size - 1
    for i in range(key_size):
        for j in range(key_size):
            temp_key[j][reverse_i] = _key[i][j]
            # print("temp_key["+str(j)+"]["+str(reverse_i)+"]=_key["+str(i)+"]["+str(j)+"]="+str(_key[i][j]))
        reverse_i -= 1
    return temp_key
#  background를 생성하고 key를 먼저 넣어줍니다. key를 먼저 넣어주는 이유는 lock을 background에 넣을 때 lock + key 값을 같이 확인하기 위해서이다.
#  lock+key가 비어있음(0) 또는 돌기가 겹침(2)인 경우에는 False를 return합니다. 모두 1인 경우엔 True를 return.

#  background의 경우 lock의 3배를 하지 않고, lock길이 + (key의 길이 - 1)*2로 하면 처음부터 겹치게 해서 값을 비교할 수 있음.
def is_unlock(bg_size, _lock, _key, start_x, start_y, c_start, c_end):
    bg = [[0] * bg_size for i in range(0, bg_size)]

    for i in range(0, len(_key)):
        for j in range(0, len(_key)):
            bg[start_y + i][start_x + j] += _key[i][j]


    for i in range(c_start, c_end):
        for j in range(c_start, c_end):
            bg[i][j] += _lock[i - c_start][j - c_start]

            if bg[i][j] != 1:
                return False
    print(bg)
    return True

def unlock(_lock, _key):
    lock_size = len(_lock)
    c_start = len(_key) - 1
    c_end = c_start + lock_size
    bg_size = lock_size + (2*c_start)

    for x in range(0, 4): # lotate 0 -> 90 -> 180 -> 270
        for i in range(0, c_end):
            for j in range(0, c_end):
                if is_unlock(bg_size, _lock, _key, i, j, c_start, c_end) is True:
                    return True
        _key = lotate(_key)

    return False

if __name__ == "__main__":

    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

    print(unlock(lock, key))
