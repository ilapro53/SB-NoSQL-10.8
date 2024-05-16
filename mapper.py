
import sys
import pandas as pd

COUNT_SKIPPED = True

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

columns = [
    'session_id',
    'session_position',
    'session_length',
    'track_id_clean',
    'skip_1',
    'skip_2',
    'skip_3',
    'not_skipped',
    'context_switch',
    'no_pause_before_play',
    'short_pause_before_play',
    'long_pause_before_play',
    'hist_user_behavior_n_seekfwd',
    'hist_user_behavior_n_seekback',
    'hist_user_behavior_is_shuffle',
    'hour_of_day',
    'date',
    'premium',
    'context_type',
    'hist_user_behavior_reason_start',
    'hist_user_behavior_reason_end',
]

head = ','.join(columns)

def read_line(line, names, sep=',', **kwargs):
    return pd.read_table(StringIO(line), sep=sep, names=names, **kwargs).iloc[0]


for line in sys.stdin:
    # line - строки из файла spotify/log_mini.csv
    
    if line.startswith(head):
        continue
    
    line = read_line(line, names=columns, usecols=['track_id_clean', 'not_skipped'])
    
    if COUNT_SKIPPED:
        count = 1
    elif line['not_skipped']:
        count = 1
    else:
        count = 0
    
    print('{track_id}\t{count}'.format(
        track_id=line['track_id_clean'],
        count=count
    )) # Выведите строки на поток вывода: <track_id>\t1