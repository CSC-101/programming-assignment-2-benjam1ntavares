from typing import Optional

import data

# Write your functions for each part in the space below.

# Part 1
#######################################################################################################################
# function create_rectangle will take two inputs of the point Parameter, and it will use them to return a Rectangle
# object without making any assumptions about the input points.

# - 1. find the lowest x value to become the x coordinate of top left
# - 2. find the highest y coordinate to become the y coordinate of top left
# - 3. define remaining coordinates accordingly

def create_rectangle(point1:data.Point, point2:data.Point)->data.Rectangle:
    tl_point = data.Point(min(point1.x, point2.x), max(point1.y, point2.y))
    br_point = data.Point(max(point1.x, point2.x), min(point1.y, point2.y))
    return data.Rectangle(tl_point, br_point)


# Part 2
########################################################################################################################
# shorter_duration_than compares two Duration objects and returns a boolean output that specifies if the first duration
#input is shorter than the second, it will most likely be used as a helper function in the future
# I will be creating a helper funciton to return duration in a float value
def seconds_and_minutes(duration:data.Duration)->float:
    minutes = duration.minutes
    seconds = duration.seconds
    if seconds >= 60:
        minutes += seconds // 60
        seconds = (seconds % 60)*10**-2
    elif seconds < 60:
        seconds = seconds*10**-2
    return seconds + minutes


def shorter_duration_than(duration1:data.Duration, duration2:data.Duration)->bool:
    return seconds_and_minutes(duration1) < seconds_and_minutes(duration2)


# Part 3
#######################################################################################################################
# the function song_shorter_than will take two parameters, the first is a list of Song objects, the second is a Duration
# object that will be used to compare to the songs in the list. The funciton will filter the input list to return a new
# list of all of the songs in the original list that are less than the specified duration.

# above I have also created seconds_and_minutes helper function to return a float value of seconds of minutes for easy
# comparison in shorter duration than. It will also make it so if the duration of the song is defined with more than 60
# seconds it will add the seconds to the minutes when comparing two Duration values

def song_shorter_than(songs:list[data.Song], inp_duration:data.Duration)->list[data.Song]:
    filtered_songs = []
    for song in songs:
        if shorter_duration_than(song.duration, inp_duration):
            filtered_songs.append(song)
    return filtered_songs

# Part 4
########################################################################################################################
# the function running_time will take two parameters, a list of Song objects, and a list of integers. The list of ints.
# essentially the list of ints represents songs in a playlist. the second list corresponds to the song's number in the
# first list. the function will return a Duration that is the sum of the total running time of the playlis.

def running_time(songs: list[data.Song], playlist: list[int])->data.Duration:
    total_time = data.Duration(0,0)
    for num in playlist:
        total_time.minutes +=  songs[num].duration.minutes
        total_time.seconds +=  songs[num].duration.seconds
    if total_time.seconds >= 60:
        total_time.minutes += total_time.seconds // 60
        total_time.seconds = (total_time.seconds % 60)
    return total_time

# Part 5
########################################################################################################################
# funciton validate_route takes two parameters, a nested list of linked cities, linked_cities: list[list[str]]] and a
# route: list[str], essentially it will help us determine if we can take a route from city to city
# An empty route will return False, a Route of Length 1 will return true.


def validate_route(linked_cities:list[list[str]], route:list[str])-> Optional[bool]:
    if len(route) == 0:
        return False

    if len(route) == 1:
        return True

    for i in range(len(route)-1):
        if [route[i],route[i+1]] not in linked_cities and [route[i+1],route[i]] not in linked_cities:
            return False
        else:
            return True


# Part 6
#######################################################################################################################
# longest_repetition will take a list of integers, and it will find the longest repetition of a single number in the
# the list. It will then return the index at which the longest repetition starts
# the function will use a while loop, and a series of if statements to perform the task. Current values will be stored
# outside of the while loop. such values will be manipulated based on the current int in the list, the next int in the
# list, and the current value of the longest repeated number

def longest_repetition(list_of_ints:list[int])->Optional[int]:
    longest_reps = 0
    longest_reps_index = 0
    current_index = 0
    current_reps = 1

    while current_index < len(list_of_ints)-1:
        if list_of_ints[current_index] == list_of_ints[current_index+1]:
            current_index += 1
            current_reps += 1
        else:
            if current_reps > longest_reps:
                longest_reps = current_reps
                longest_reps_index = current_index-(current_reps-1)
                current_reps = 1
                current_index += 1
            elif current_reps == longest_reps:
                longest_reps_index = None
                current_index += 1

            else:
                current_reps = 1
                current_index += 1
    if current_reps > longest_reps:
        longest_reps_index = current_index-(current_reps-1)
    return longest_reps_index


