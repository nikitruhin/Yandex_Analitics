import random
import statistics


def simulate_playlist_search(num_trials, p_favorite, p_hiphop_given_favorite):
    tracks_until_favorite_hiphop = []
    for i in range(num_trials):
        track_count = 0
        found_favorite_hiphop = False
        while not found_favorite_hiphop:
            track_count += 1
            #Случайный трек стал любимым(Нормальное распределение)
            is_favorite = random.random() < p_favorite
            if is_favorite:
                #Любимый трек - хип-хоп(Нормальное распределение)
                is_hiphop = random.random() < p_hiphop_given_favorite
                if is_hiphop:
                    found_favorite_hiphop = True
        tracks_until_favorite_hiphop.append(track_count)
    return tracks_until_favorite_hiphop


def analyze_simulation_results(tracks_list, track_duration_minutes):
    time_minutes_list = [track_count * track_duration_minutes for track_count in tracks_list]
    mean_time = statistics.mean(time_minutes_list)
    print(f"\nСреднее время поиска (секунды): {mean_time * 60}")

num_trials = 10000000  #Количество симуляций
p_favorite = 0.2 #Параметр1
p_hiphop_given_favorite = 1/3 #Параметр2
track_duration_minutes = (2 * 60 + 45) / 60 
tracks_to_find = simulate_playlist_search(num_trials, p_favorite, p_hiphop_given_favorite)
analyze_simulation_results(tracks_to_find, track_duration_minutes)
