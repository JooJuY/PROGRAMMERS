def solution(genres, plays):
    answer = []
    genre = []
    for g in range(len(genres)):
        for i in range(len(genre)):
            if genre[i][0] == genres[g]:
                genre[i][1].append(g)
                break
        else:
            genre.append([genres[g], [g]])
    genre.sort(key=lambda x: -len(x[1]))



    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))