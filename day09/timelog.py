import sys
import re
import funcs as d9
from collections import defaultdict

try:
    log_file = sys.argv[1]
except IndexError:
    print("No file supplied")
    exit()

with open(log_file, "r") as fh_read: #fh = file handler
    log_list = fh_read.readlines()

output_file = log_file.replace(".log", ".txt")

list_of_dicts = d9.list_of_dicts(log_list)
duration = d9.make_duration_dict(list_of_dicts)

# Adding percent time occupied as a column
total_duration = sum(list(duration.values()))
for activity in duration:
    duration[activity] = [
        duration[activity], int(duration[activity]*100/total_duration)
        ]

sorted_duration = d9.sort_by_keys(duration)

# The below loop writes out output split across days as:
# <start HH:MM> - <end HH:MM> <activity>
# Following this, it writes out the time data as:
# <activity> <duration across days> minutes <percent time>%
with open(output_file, "w") as fh_write:
    for dict in list_of_dicts:
        for index, time in enumerate(dict):
            if dict[time] == 'End\n':
                continue
            fh_write.write(f"{time} - {list(dict.keys())[index + 1]}: {dict[time]}")
        fh_write.write("\n")
    for activity in sorted_duration:
        fh_write.write(f"{activity.replace('\n',''):<20}{sorted_duration[activity][0]:>4} minutes {sorted_duration[activity][1]:>3}%\n")