# Реализуйте код обработки результата MapReduce
import sys, json

ORDERED_BY_ID = False

uniq_tracks_count = 0
popular_tracks_count = 0
top_2_tracks = [None, None]
uniq_tracks = set()


for line in sys.stdin:
    # line - результат работы MapReduce, финальный формат от reducer.py - <track_id>\t<N>
    track_id, count = line.strip().split('\t')
    count = int(count)
    
    uniq_tracks_count += 1
    
    if top_2_tracks[0] is None:
        top_2_tracks[0] = track_id, count
    elif (top_2_tracks[1] is None) and (top_2_tracks[0][1] >= count):
        top_2_tracks[1] = track_id, count
    elif top_2_tracks[0][1] < count:
        top_2_tracks[1] = top_2_tracks[0]
        top_2_tracks[0] = track_id, count
    
    if count > 20:
        if ORDERED_BY_ID:
            popular_tracks_count += 1
        else:
            uniq_tracks.add(track_id)

uniq_tracks_count = len(uniq_tracks)

data = {
    'q1': uniq_tracks_count,
    'q2': popular_tracks_count,
    'q3': top_2_tracks,
}

with open('result.json', 'w') as f:
    f.write(json.dumps(data))