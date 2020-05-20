# # https://hello70825.tistory.com/82
#
from collections import deque
n, m = map(int, input().split())
S=[list(map(int, [input()])) for k in range(n)]
print(S)


# map을 사용하여 정수로 변환하기
# split의 결과를 매번 int로 변환해주기엔 귀찮기 때문에 map에 int와 input().split()을 ㄶ으면
# split의 결과를 모두 int로 변환해줍니다.

# 파라미터를 몇 개를 받을 지 모르는 경우 사용한다. args는 튜플 형태로 전달된다.
# def print_param(*args):
#     print args
#     for p in args:
#         print p

# 값을 여러 개 출력하기
# print에는 변수나 값 여러 개를, (콤마)로 구분하여 넣을 수 있습니다.
# print에 변수나 값을 콤마로 구분해서 넣으면 각 값이 공백으로 띄워져서 한 줄로 출력됩니다.
# 이제 값을 여러 개 출력할 때 print 함수를 여러 번 쓰지 않아도 됩니다.

# sep로 값 사이에 문자 넣기
# 값 사이에 공백이 아닌 다른 문자를 넣고 싶을 수도 있습니다. 이때는 다음과 같이 print의 sep에 문자 또는 문자열을 지정해주면 출력됩니다
# (sep는 구분자라는 뜻의 seperator에서 따왔습니다.)

# end로 문자열 맨 뒤 사용
# print(1, end='')
# print(2, end='')
# end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
# 기본적으로 print의 end에 \n이 지정된 상태인데 빈 문자열을 지정하면 강제 \n을 지워주기 때문
# 즉, end는 현재 print가 끝난 뒤 그 다음에 오는 print 함수에 영향을 줍니다.

# Boolean 비교 연산자 사용
# True, Fasle로 표현
# ==(equal), !=(not equal)으로 같은 지 다른 지 비교 가능
# 숫자, 문자열 같은 지 다른 지 비교 가능
# 문자열같은 경우 비교할 때 대소문자를 구분합니다.
# 단어가 같아도 대소문자가 다르면 다른 문자열로 판단합니다.

# 객체가 같은지 다른지 비교하기
# ==, !=는 값 자체를 비교하고 is, is not은 객체(object)를 비교
# 1 == 1.0 -> True
# 1 is 1.0 -> False (정수 객체와 실수 객체를 비교)
# id : 객체의 고유한 값(메모리 주소)을 구합니다.(이 값은 파이썬을 실행하는 동안에는 계속 유지되며 다시 실행하면 달라집니다.)
# id(1) 과 id(1.0)은 다른 값이므로 서로 다른 객체임을 알 수 있다.

# 논리 연산자
# and, or, not
# 정수 1은 True, 0은 False

# 단락 평가(short-circuit evaluation)
# 첫 번째 값만으로 결과가 확실할 때 두 번째 값은 확인(평가)하지 않는 방법을 말한다.
# 즉, and 연산자는 두 값이 모두 참이어야 참이므로 첫 번째 값이 거짓이면 두 번째 값은 확인하지 않고 바로 거짓으로 결정합니다.
# or 연산자는 두 값 중 하나만 참이라도 참이므로 첫 번째 값이 참이면 두 번째 값은 확인하지 않고 바로 참으로 결정합니다.

# True and 'Python' -> 'Python'
# 문자열 'Python'도 bool로 따지면 True라서 True and True가 되어 True가 나올 것 같지만 'Python'이 나왔습니다.
# 왜냐하면 파이썬에서 논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환하기 때문입니다.
# 따라서 논리 연산자는 무조건 bool을 반환하지 않습니다.

# 'Python' and True -> True
# False and 'Python' -> False
# 0 and 'Python' -> 0 : 0은 False 이므로 and 연산자는 두 번째 값을 평가하지 않음
# True or 'Python' -> True
# 'Python' or True -> 'Python'
# False or 'Python' -> 'Python'
# 0 or False -> False

# D=[[[-1]*2 for j in range(m)] for i in range(n)]
# D[0][0][0] = 1
# q = deque()
# q.append((0, 0, 0))
# dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
#
# while q:
#     x, y, z=q.popleft()
#     for i in range(4):
#         nx, ny=x+dx[i], y+dy[i]
#         if 0<=nx<n and 0<=ny<m:
#             if S[nx][ny]==0 and D[nx][ny][z] == -1:
#                 D[nx][ny][z]=D[x][y][z]+1
#                 q.append((nx, ny, z))
#             if z==0 and S[nx][ny]==1 and D[nx][ny][z+1]==-1:
#                 D[nx][ny][z+1]=D[x][y][z]+1
#                 q.append((nx, ny, z+1))
# if D[n-1][m-1][0]==-1:
#     print(D[n-1][m-1][1])
# elif D[n-1][m-1][1]==-1:
#     print(D[n-1][m-1][0])
# else:
#     print(min(D[n-1][m-1]))
