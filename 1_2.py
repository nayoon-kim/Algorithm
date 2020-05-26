
def eat(pack, str, num, l):
    if len(str) == num:
        s = ''.join(str)
        if not s in l:
            l.append(s)
        return
    for p in pack:
        if pack[p] == 0:
            pack[p] = 1
            str.append('K')
            eat(pack, str, num, l)
            del str[-1]
            pack[p] = 0
        elif 0<pack[p]<3:
            pack[p]+=1
            str.append('R')
            eat(pack, str, num, l)
            del str[-1]
            pack[p]-=1


def solution(a):
    pack = dict()
    for i in range(a):
        pack[i] = 0
    str = []
    l = []
    eat(pack, str, a*3, l)

    return len(l)



a = 2
print(solution(3))

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()

# def eat(pack, st, num, l):
# 	if len(st) == num * 3:
# 		s = ''.join(st)
# 		if not s in l:
# 			l.append(s)
# 			return
#
# 	for p in pack:
# 		if pack[p] == 0:
# 			pack[p] = 1
# 			st.append('K')
# 			eat(pack, st, num, l)
# 			del st[-1]
# 			pack[p] = 0
# 		elif 0<pack[p]<3:
# 			pack[p]+=1
# 			st.append('R')
# 			eat(pack, st, num, l)
# 			del st[-1]
# 			pack[p] -= 1
#
# def solution(user_input):
# 	pack = dict()
# 	for i in range(user_input):
# 		pack[i] = 0
# 	st = []
# 	l = []
# 	eat(pack, st, user_input, l)
#
# 	return len(l)
#
# print(solution(int(user_input)))
