import numpy as np
import sys


changes = list(np.loadtxt('frequencies.txt', dtype=int))
frequencies = [0]
total = 0

test = True
while test:
    for item in changes:
        total += item
        if total in frequencies:
            print(total)
            sys.exit()
        else:
            frequencies.append(total)
    


print(np.sum(changes))
