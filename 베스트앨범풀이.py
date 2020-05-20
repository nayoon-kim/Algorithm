# from collections import defaultdict
# from operator import itemgetter
# def solution(genres, plays):
#     genre_play_dict = defaultdict(lambda:0)
#     for genre, play in zip(genres, plays):
#         genre_play_dict[genre] += play
#
#     genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]
#
#     final_dict = defaultdict(lambda: [])
#     for i, genre_play_tuple in enumerate(zip(genres, plays)):
#         final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))
#
#     answer = []
#     for genre in genre_rank:
#         one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
#         if len(one_genre_list) > 1:
#             answer.append(one_genre_list[0][1])
#             answer.append(one_genre_list[1][1])
#         else:
#             answer.append(one_genre_list[0][1])
#
#     return answer
#
# def solution(genres, plays):
#     answer = []
#     dic = {}
#     album_list = []
#     for i in range(len(genres)):
#         dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
#         album_list.append(album(genres[i], plays[i], i))
#
#     dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
#     album_list = sorted(album_list, reverse=True)
#
#
#     while len(dic) > 0:
#         play_genre = dic.pop(0)
#         print(play_genre)
#         cnt = 0
#         for ab in album_list:
#             if play_genre[0] == ab.genre:
#                 answer.append(ab.track)
#                 cnt+=1
#             if cnt == 2:
#                 break
#
#     return answer
#
# class album:
#     def __init__(self, genre, play, track):
#         self.genre = genre
#         self.play = play
#         self.track = track
#
#     def __lt__(self, other):
#         return self.play < other.play
#     def __le__(self, other):
#         return self.play <= other.play
#     def __gt__(self, other):
#         return self.play > other.play
#     def __ge__(self, other):
#         return self.play >= other.play
#     def __eq__(self, other):
#         return self.play == other.play
#     def __ne__(self, other):
#         return self.play != other.play

def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    # 어려웡..
    genreSort = sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0], d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key= lambda x: (x[0], -x[1]), reverse=True)]
        print(temp)
        answer += temp[:min(len(temp), 2)]

    return answer

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

solution(genres, plays)
# print(solution(genres, plays))
