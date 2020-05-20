# 크루스칼 알고리즘으로
# 최소 스패닝 트리를 만든다.

# * 최소 스패닝 트리란
# 정점이 n개인 그래프의 간선 중 일부인 n-1개의 간선을 선택해서 모든 정점을
# 연결한 트리 중 가중치의 합이 최소인 트리

# * 크루스칼 알고리즘
# 최소 스패닝 트리를 찾는 알고리즘

def getParent(arr, x):
    if arr[x] == x:
        return x
    return arr[x] = getParent(arr, arr[x])

def unionParent(arr, a, b):
    a = getParent(arr, a)
    b = getParent(arr, b)

    if a < b:
        arr[b] = a
    else:
        arr[a] = b

def find(arr, a, b):
    a = getParent(arr, a)
    b = getParent(arr, b)
    if a == b:
        return 1
    else:
        return 0

class Edge:
    def __init__(self, a, b, distance):
        self.node[0] = a
        self.node[1] = b
        self.distance = distance
    def __lt__(self, other):
        return self.distance < other.distance

def solution(n, costs):
    answer = 0

    connected = []
    con = list(range(0, n))
    costs = sorted(costs)

    for c in costs:
        connected.append(Edge(c[0], c[1], c[2]))
    print(con)

    return answer



# class Node:
#
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None
#
#     def size(self):
#         l = self.left.size() if self.left else 0
#         r = self.right.size() if self.right else 0
#         return l + r + 1
#
#     def depth(self):
#         leftDepth = self.left.depth() if self.left else 0
#         rightDepth = self.right.depth() if self.right else 0
#         return leftDepth+1 if leftDepth >rightDepth else rightDepth+1
#
# class BinaryTree:
#
#     def __init__(self, r):
#         self.root = r
#
#     def size(self):
#         if self.root: return self.root.size()
#         else: return 0
#
#     def depth(self):
#         if self.root: return self.root.depth()
#         else: return 0

costs=[[2,3,8],[0,2,2],[1,3,1],[1,2,5],[0,1,1]]
solution(4, costs)
