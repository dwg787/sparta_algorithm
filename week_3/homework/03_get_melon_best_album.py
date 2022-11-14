genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
#Dictionary로 푸는 문제

def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_idx_play_arr_dict = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_idx_play_arr_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_idx_play_arr_dict[genre].append([i, play])

    print(genre_total_play_dict)
    print(genre_idx_play_arr_dict)
    sorted_genre_play_arr = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_genre_play_arr)
    result = []
    for genre, _value in sorted_genre_play_arr:
        idx_play_arr = genre_idx_play_arr_dict[genre]
        sorted_idx_play_arr = sorted(idx_play_arr, key=lambda item: item[1], reverse=True)
        print(sorted_idx_play_arr)

        for i in range(len(sorted_idx_play_arr)):
            if i > 1:
                break
            result.append(sorted_idx_play_arr[i][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!