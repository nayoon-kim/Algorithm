def bt(word, target, visited, words, num, result):
    if word == target:
        result.append(num)
    for word_index, w in enumerate(words):
        count = 0
        if visited[word_index] == 1:
            continue
        for i, b in enumerate(word):
            if w[i] == b:
                count += 1
        if count == len(word) - 1:
            v = visited.copy()
            v[word_index] = 1
            n = num.copy()
            n.append(w)
            bt(w, target, v, words,n, result)

def solution(begin, target, words):
    answer = len(words)
    visited = [0 for i in words]

    if not target in words:
        return answer

    num = []
    result = []
    bt(begin, target, visited, words, num, result)

    for r in result:
        if len(r) < answer:
            answer = len(r)
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
