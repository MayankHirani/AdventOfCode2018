import string
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan)

with open('coordinates.txt') as f:
        coordinates = [line.strip() for line in f.readlines()]

values = {}

# Letter creation
letters = []
for letter in string.ascii_uppercase:
    letters.append(letter)
    letters.append(letter * 2)
#

for index, coordinate in enumerate(coordinates):
    x = coordinate.split(',')[0]
    y = coordinate.split(',')[1].strip()
    values[letters[index]] = ( int(x), int(y) )

grid = np.full((400, 400), '  ')

for value in values:
    grid[values[value][0], values[value][1]] = value

plt.plot(grid)
plt.show()
