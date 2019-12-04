import time
import operator
from collections import Counter

#guard with most minutes is 1901
def part1():
    with open('guards.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    advent_list.sort()
    dict_of_guards = {}
    guard_num = 0
    start_time = 0
    end_time = 0
    for timestamp in advent_list:
        if timestamp[19] == "G":
            guard_num = timestamp.split(" ")[3]
        elif timestamp[19] == "f":
            start_time = timestamp[12:14] + timestamp[15:17]
        elif timestamp[19] == "w":
            end_time = timestamp[12:14] + timestamp[15:17]
            difference_hours = int(end_time[0:2]) - int(start_time[0:2])
            difference_hours_conv = difference_hours * 60
            difference_minutes = int(end_time[2:4]) - int(start_time[2:4])
            if guard_num in dict_of_guards:
                dict_of_guards[guard_num] += difference_minutes + difference_hours_conv
            else:
                dict_of_guards[guard_num] = difference_minutes + difference_hours_conv
    
    print(max(dict_of_guards.items(), key = operator.itemgetter(1))[0])

def part1cont(guard_num):
    with open('guards.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    advent_list.sort()
    dict_of_guards = {}
    guard_num = 0
    start_time = 0
    end_time = 0
    minutes_dict = {}
    for num in range(0, 60):
        minutes_dict[num] = 0
    wrong_guard = True
    for timestamp in advent_list:
        if timestamp[26:30] == guard_num:
            wrong_guard = False
                
        elif timestamp[19] == "G" and timestamp[26:30] != guard_num:
            wrong_guard = True
            
        if wrong_guard == False:
            if timestamp[19] == "f":
                start_time = timestamp[12:14] + timestamp[15:17]
            elif timestamp[19] == "w":
                end_time = timestamp[12:14] + timestamp[15:17]
                for minute in range(int(start_time[2:4]), int(end_time[2:4])):
                    minutes_dict[minute] += 1
                    print(minutes_dict)
    return max(minutes_dict.items(), key = operator.itemgetter(1))[0]

def part2():
    with open('guards.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    advent_list.sort()

    guards = []

    for item in advent_list:
        if item[19] == 'G':
            guard_name = item.split(" ")[3]
            if guard_name not in guards:
                guards.append(guard_name)

    print(guards)

    highest_min = {}
    
    
    for guard in guards:
        minutes_dict = {}
        for item in advent_list:
            if item[26:30] == guard:
                wrong_guard = False
                
            elif item[19] == "G" and item[26:30] != guard:
                wrong_guard = True
            
                if wrong_guard == False:
                    if item[19] == "f":
                        start_time = item[12:14] + item[15:17]
                    elif item[19] == "w":
                        end_time = item[12:14] + item[15:17]
                        for minute in range(int(start_time[2:4]), int(end_time[2:4])):
                            minutes_dict[minute] += 1

        print(minutes_dict)
        highest_min[guard] = max(minutes_dict.items(), key = operator.itemgetter(1))[0]

    print(highest_min)

part2()
