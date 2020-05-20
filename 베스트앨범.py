from collections import OrderedDict
def solution(genres, plays):
    answer = []

    genre = {}

    for g, p in zip(genres, plays):
        if g in genre:
            genre[g]+=p
        else:
            genre[g]=p

    genre = dict(OrderedDict(sorted(genre.items(), key=lambda x:x[1], reverse=True)))
    print(genre)
    info = dict()
    for gen in genre:
        max = 0
        max_before = 0
        max_num, max_before_num = 0, 0
        song_num = 0
        for p_n, g in enumerate(genres):
            if gen == g:
                if max < plays[p_n]:
                    if max_before < max:
                        max_before = max
                        max_before_num = max_num
                    elif max_before == max:
                        max_before_num = max_num if max_before_num > max_num else max_before_num
                    max = plays[p_n]
                    max_num = p_n
                elif max == plays[p_n]:
                    if max > max_before:
                        max_before = plays[p_n]
                        max_before_num = p_n
                else:
                    if max_before < plays[p_n]:
                        max_before = plays[p_n]
                        max_before_num = p_n
                song_num+=1
        answer.append(max_num)
        if song_num > 1:
            answer.append(max_before_num)


    return answer

genres=["classic", "pop", "classic",  "pop","classic","classic"]
plays=[400, 600, 150, 2500, 500, 500]

print(solution(genres, plays))
