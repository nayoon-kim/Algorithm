from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue
        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1: # word의 길이가 다 다르기 때문에 다를 경우 count += 1을 해줘서 한번에 한 글자씩만 바꿀 수 있도록 한다.
            yield word
# return sends a specified value back to its caller
# yield can produce a sequence of values


def solution(begin, target, words):
    dist = {begin: 0} # -> dictionary 선언
    queue = deque([begin]) # -> queue에 ["hit"]와 같이 리스트를 넣음

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)
    return dist.get(target, 0)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
