# Реализуйте код обработки результата MapReduce
import sys, json

uniq_tracks_count = 0
uniq_tracks = dict()
popular_tracks_count = 0

top_2_tracks = [None, None]


for line in sys.stdin:
    # Парсинг результата работы MapReduce (финальный формат от reducer.py - <track_id>\t<N>)
    track_id, count = line.strip().split('\t')
    count = int(count)
    
    # Подсчет уникальных треков
    if not (track_id in uniq_tracks):
        uniq_tracks[track_id] = 0
    count_before = uniq_tracks[track_id]
    uniq_tracks[track_id] += count
    
    # Подсчет популярных треков
    if (uniq_tracks[track_id] > 20) and (count_before <= 20):
        popular_tracks_count += 1
    
    # Топ 2 трека
    total_count = uniq_tracks[track_id]
    if top_2_tracks[0] is None:
        top_2_tracks[0] = track_id, total_count
    elif (top_2_tracks[1] is None) and (top_2_tracks[0][1] >= total_count):
        top_2_tracks[1] = track_id, total_count
    elif top_2_tracks[0][1] < total_count:
        top_2_tracks[1] = top_2_tracks[0]
        top_2_tracks[0] = track_id, total_count
        
uniq_tracks_count = len(uniq_tracks)

data = {
    'q1': uniq_tracks_count,
    'q2': popular_tracks_count,
    'q3': top_2_tracks,
}

with open('result.json', 'w') as f:
    f.write(json.dumps(data))