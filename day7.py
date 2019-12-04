
order = ""

with open('order.txt') as f:
        order = [line.strip() for line in f.readlines()]

pre_steps = []
current_steps = []

for step in order:
    pre_step = step.split()[1]
    current_step = step.split()[7]
    pre_steps.append(pre_step)
    current_steps.append(current_step)
    
print(pre_steps)
print(current_steps)

for thing in current_steps:
    if thing not in pre_steps:
        print(thing)

for thing in pre_steps:
    if thing not in current_steps:
        print(thing)

