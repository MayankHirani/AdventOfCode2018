import numpy as np
import sys

fabrics = []
fabric = open('fabric.txt', 'r')
for line in fabric:
    fabrics.append(str(line.strip()))
    
x = []
y = []
width = []
height = []
coordinates = {}

grid = np.zeros((1000, 1000), dtype=int)
bigList = []

        
for thing in fabrics:
    at = thing.index('@')
    idNum = int(thing[1:at - 1])
    bigList.append(idNum)
    
for item in fabrics:
    comma = item.index(',')
    at = item.index('@')
    colon = item.index(':')
    multi = item.index('x')


    x = int(item[at + 2:comma])
    y = int(item[comma+1:colon])
    width = int(item[colon+2:multi])
    height = int(item[multi+1:])
    for part in grid[y:y+height, x:x+width]:
        for num in part:
            #print(num)
            if num >= 1:
                if idNum in bigList:
                    bigList.remove(idNum)
    print(grid[y:y+height, x:x+width])            
    grid[y:y+height, x:x+width] += 1



counter = 0
for item in np.nditer(grid):
    if item > 1:
        counter += 1

for index, item in np.ndenumerate(grid):
    if item == 1:
        for thing in fabrics:
            comma = thing.index(',')
            at = thing.index('@')
            colon = thing.index(':')
            multi = thing.index('x')
            x = int(thing[at + 2:comma])
            y = int(thing[comma+1:colon])
            width = int(thing[colon+2:multi])
            height = int(thing[multi+1:])
            if index[0] >= y and index[0] <= y + height:
                if index[1] >= x and index[1] <= x + width:
#                    print(thing)
                    sys.exit()
        sys.exit()
