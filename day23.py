import numpy as np
import sys
import re

with open('nanobots.txt') as f:
        nanobots = [line.strip() for line in f.readlines()]

# 99391187 Is Highest Radius
        
signals = []
coordinates = []

def check(list1, list2):
    if ( abs(list1[0] - list2[0]) + abs(list1[1] - list2[1]) + abs(list1[2] - list2[2])) > 99391187:
        return False
    else:
        return True
    
for item in nanobots:
    carrot = item.index('>')
    other_carrot = item.index('<')
    signals.append(int(item[carrot+5:]))

    split_item = item.split(',')

    coordinate1 = int(split_item[0][split_item[0].index('<')+1:])
    coordinate2 = int(split_item[1])
    coordinate3 = int(split_item[2][:split_item[2].index('>')])

    coordinates.append([coordinate1, coordinate2, coordinate3])
    
    if int(item[carrot+5:]) == 99391187:
        saved_coord = [coordinate1, coordinate2, coordinate3]
        break

counter = 0
for item in nanobots:
    
    split_item = item.split(',')
    coordinate1 = int(split_item[0][split_item[0].index('<')+1:])
    coordinate2 = int(split_item[1])
    coordinate3 = int(split_item[2][:split_item[2].index('>')])

    if check([coordinate1, coordinate2, coordinate3], [-65489612, 1848244, 21168921]):
        counter += 1
    

print(coordinates)
    

print(counter)
