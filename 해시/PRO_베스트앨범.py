def solution(genres, plays):
    answer = []
    genre = []
    for g in range(len(genres)):
        for i in range(len(genre)):
            if genre[i][0] == genres[g]:
                genre[i][1].append(g)
                genre[i][2] += plays[g]
                break
        else:
            genre.append([genres[g], [g], plays[g]])
    # 많이 들은 장르 순으로 정렬
    genre.sort(key=lambda x: -x[2])
    # 장르 안에서 많이 들은 노래 순으로 정렬해 앞에 2곡만 answer에 저장
    for lst in genre:
        lst[1].sort(key=lambda x: -plays[x])
        answer += lst[1][:2]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))