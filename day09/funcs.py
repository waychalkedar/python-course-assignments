import sys
import re
from collections import defaultdict

def hhmm_to_minutes(time):
    """
    Function to convert time supplied as a string in the HH:MM format to 
    time in minutes (as an integer).
    >>> hhmm_to_minutes('01:30')
    90
    >>> hhmm_to_minutes('16:15')
    975
    """
    match1 = re.search(r'[0-9]{2}:[0-9]{2}', time)
    if match1:
        split_time = time.split(':')
        minutes = int(split_time[0])*60 + int(split_time[1])
        return minutes
    else:
        print("Incorrect time format.")
        return None

def list_of_dicts(log_list):
    """
    Given the .log file stored as a list of lines, makes a list of dictionaries.
    Each dictionary contains entries for one day.
    A new dictionary is initialized when a new line is present (i.e. a new day's entry begins)
    """
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
    
    return list_of_dicts

def make_duration_dict(list_of_dicts):
    """
    Makes a dictionary containing key-value pairs as 
    {<activity>: <duration (in minutes)>}
    along with percent of total duration
    """
    # To store the duration of each activity tallied across days,
    # we initialize a dictionary with default values being 0
    duration = defaultdict(int)

    for dict in list_of_dicts:
        for index, time in enumerate(dict):
            if dict[time] == 'End\n':
                break
            duration[dict[time]] += ( hhmm_to_minutes(list(dict.keys())[index + 1]) 
                                    - hhmm_to_minutes(list(dict.keys())[index]) )
    
    return duration

def sort_by_keys(duration):
    """
    Returns a new dictionary sorted in alphabetical order of its keys
    """
    sorted_duration = {}
    for activity in sorted(duration):
        sorted_duration[activity] = duration[activity]
    
    return sorted_duration
