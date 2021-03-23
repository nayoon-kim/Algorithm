import re

def solution(new_id):
    answer = ''
    # level 1
    new_id = new_id.lower()
    

    # re.sub(정규식, 바꿀 문자, 변경할 문자열) - 치환

    # level 2
    p2 = re.sub(r"[^a-zA-Z0-9\-\_\.]", "", new_id)
    # for m in p2.findall(new_id):
    #     print(m)
    # level 3
    p = re.sub(r"[\.]+", ".", new_id)
    print(p)
    # for m in p.finditer(new_id):
    #     print(m)
    # level 4
    new_id.strip('.')
    
    # # level 5
    # if len(new_id) == 0:
    #     new_id = "a"
    
    # # level 6
    # if len(new_id) > 15:
    #     new_id = new_id[:16]
    #     if new_id[-1] == '.':
    #         del new_id[-1]
    
    # # level 7
    # if len(new_id) <= 2:
    #     while len(new_id) != 3:
    #         new_id += new_id[-1]
    # return answer

solution("...!@BaT#*..y.abcdefghijklm")


def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st