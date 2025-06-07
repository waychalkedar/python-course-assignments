import sys
import re
from collections import defaultdict

def hhmm_to_minutes(time):
    """
    Function to convert time supplied as a string in the HH:MM format to 
    time in minutes (as an integer)
    """
    split_time = time.split(':')
    minutes = int(split_time[0])*60 + int(split_time[1])
    return minutes

try:
    log_file = sys.argv[1]
except IndexError:
    print("No file supplied.")
    exit()

with open(log_file, "r") as fh_read: #fh = file handler
    log_list = fh_read.readlines()

output_file = log_file.replace(".log", ".txt")

# Because we ideally don't know how many days are captured in the log, 
# we make a list of dictionaries. This list has only one empty dictionary, 
# but when a new day occurs in the log (captured by the current line being only '\n'),
# a new dictionary is appended to the list. 
# The data is filled into the new dictionary
list_of_dicts = [{}]
dict_no = 0

for line in log_list:
    if line == '\n':
        list_of_dicts.append({})
        dict_no += 1
        continue
    match1 = re.search(r'[0-9]{2}:[0-9]{2}', line)
    if match1:
        list_of_dicts[dict_no][match1.group(0)] = line.replace(match1.group(0), '')[1:]

# To store the duration of each activity tallied across days,
# we initialize a dictionary with default values being 0
duration = defaultdict(int)

for dict in list_of_dicts:
    for index, time in enumerate(dict):
        if dict[time] == 'End\n':
            break
        duration[dict[time]] += ( hhmm_to_minutes(list(dict.keys())[index + 1]) 
                                 - hhmm_to_minutes(list(dict.keys())[index]) )

# We now want to add an entry for each activity corresponding to the
# percent time it occupied.
total_duration = sum(list(duration.values()))
for activity in duration:
    duration[activity] = [
        duration[activity], int(duration[activity]*100/total_duration)
        ]

# We create a new dictionary to sort the duration dictionary
# in alphabetical order of its keys, to enable a sorted output too.
sorted_duration = {}

for activity in sorted(duration):
    sorted_duration[activity] = duration[activity]

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