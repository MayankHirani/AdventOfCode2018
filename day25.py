with open('spacetime.txt') as f:
        spacetime = [line.strip() for line in f.readlines()]

constellations = []

def check(list1, list2):
    if ( abs(list1[0] - list2[0]) + abs(list1[1] - list2[1]) + abs(list1[2] - list2[2]) + abs(list1[3] - list2[3])) > 3:
        return False
    else:
        return True
        
for index, item in enumerate(spacetime):
    split_item = item.split(',')
    int_item = []
    for thing in split_item:
        int_item.append(int(thing))
    
    spacetime.remove(item)
    
    spacetime.insert(index, int_item)

did_something = True

while len(spacetime) > 0:
    if did_something:
        did_something = False
        for item in spacetime:
            in_constellation = False
    
            if len(constellations) == 0:
                constellations.append([item])
                spacetime.remove(item)
            elif in_constellation == False:
                for constellation_type in constellations:
                    if in_constellation == False:
                        for constellation in constellation_type:
                            if check(item, constellation):
                                constellation_type.append(item)
                                spacetime.remove(item)
                                in_constellation = True
                                did_something = True
                                break
    elif did_something == False:
        constellations.append([spacetime[0]])
        did_something = True


        

print(constellations)
print(len(constellations))
print(len(spacetime))

