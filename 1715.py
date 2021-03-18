# 시간초과
# from collections import deque

# n = int(input())
# card = [int(input()) for i in range(n)]

# def operation():
#     queue = deque()
#     queue.extendleft(card)
#     sum = 0
    
#     while True:
#         queue = sorted(queue, reverse=True)
#         print(queue)
#         q = queue.pop()
#         if queue:
#             p = queue.pop()
#             queue.append(p + q)
#             sum += p + q
#         else:
#             print(sum)
#             break

# operation()

from queue import PriorityQueue

n = int(input())
que = PriorityQueue()
for i in range(n):
    que.put(int(input()))
# sum = 0
# while True:
#     p = que.get()
#     if que.empty():
#         print(sum)
#         break
#     else:
#         q = que.get()
#         que.put(p + q)
#         sum += p + q

def operation():
    sum = 0
    while que.qsize() >= 2:
        temp = que.get() + que.get()
        sum += temp
        que.put(temp)
    print(sum)

operation()

