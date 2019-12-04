import numpy as np
import sys

boxes = list(np.loadtxt('boxes.txt', dtype=str))

twice = 0
three = 0





def check(item):
    value = 0
    threeDone = True
    twoDone = True
    for char in item:
        if item.count(char) == 3 and threeDone:
            if twoDone == False:
                value = 2
            else:
                value = 1
                threeDone = False
        elif item.count(char) == 2 and twoDone:
            if threeDone == False:
                value = 2
            else:
                value = 3
                twoDone = False
    return value



for item in boxes:
    if check(item) == 1:
        three += 1
    elif check(item) == 2:
        three += 1
        twice += 1
    elif check(item) == 3:
        twice += 1

print(three * twice)

for item1 in boxes:
    for item2 in boxes:
        if item1 != item2:
            counter = 0
            for x in range(0, 26):
                if item1[x] != item2[x]:
                    counter += 1
            if counter == 1:
                print(item1, item2)
                outputThing = ""
                for char in item1:
                    if char in item1 and char in item2:
                        outputThing += char
                print(outputThing)
                sys.exit()

                

        
