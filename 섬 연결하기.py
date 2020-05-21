# 크루스칼 알고리즘으로
# 최소 스패닝 트리를 만든다.

# * 최소 스패닝 트리란
# 정점이 n개인 그래프의 간선 중 일부인 n-1개의 간선을 선택해서 모든 정점을
# 연결한 트리 중 가중치의 합이 최소인 트리

# * 크루스칼 알고리즘
# 최소 스패닝 트리를 찾는 알고리즘

# https://blog.naver.com/PostView.nhn?blogId=jaeyoon_95&logNo=221872563653&categoryNo=74&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

# 탐욕적인 방법을 이용하여 그래프의 모든 정점을 최소 비용으로 연결하는 방법이다.
# 처음 시작하는 노드로부터 하나의 간선을 선택해가면 된다.
#
# 1. 0에 연결되어 있는 간선은 0-1(1), 0-2(2) 두 가지 간선이 있다.
# 최소 비용으로 연결하는 것이 목적이므로 0-1 간선을 선택하고
# 1의 노드를 연결된 노드 집합에 넣도록 한다.
# 2. 0과 1의 노드에 연결되어 있는 간선을 찾도록 하자.
# 그러면 0-2(2), 1-2(5), 1-3(1) 세 가지 간선이 존재하게 되고,
# 역시 최소를 선택하므로 1-3을 선택하게 된다.
# 3. 위와 같은 방법으로 진행을 하면 0-2 간선을 선택하게 되어 모든 노드들이 연결

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    # distance를 오름차순으로 정렬시키고, 방문을 확인하는 connection 리스트에 가장 cost가 작은 노드를 넣어줌.
    connection = [costs[0][0]]

    while len(connection) != n:
        for i, cost in enumerate(costs):
            if cost[0] in connection and cost[1] in connection: continue
            if cost[0] in connection or cost[1] in connection:
                answer += cost[2] # distance 추가
                connection.append(cost[0])
                connection.append(cost[1])
                connection = list(set(connection)) # 중복 제거
                costs.pop(i)
                break
    return answer


costs=[[2,3,8],[0,2,2],[1,3,1],[1,2,5],[0,1,1]]
print(solution(4, costs))


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
