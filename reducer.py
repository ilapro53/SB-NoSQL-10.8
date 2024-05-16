# Реализуйте reducer
import sys

current_track_id = None
current_count = 0
track_id = None

for line in sys.stdin:
    # line - группа строк из выхода mapper.py
    try:
        track_id, count = line.strip().split('\t', 1)
    except ValueError:
        continue
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_track_id == track_id:
        current_count += count
    else:
        if current_track_id:
            print(f'{current_track_id}\t{current_count}')
            
        current_count = count
        current_track_id = track_id
    
if current_track_id == track_id:
    print(f'{current_track_id}\t{current_count}')