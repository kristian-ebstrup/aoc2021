filename = "input"

pos = [0, 0, 0]        # horizontal, depth, aim

with open(filename) as f:
    for line in f.readlines():
        line = line.split()
        if line[0] == 'forward':
            pos[0] += int(line[1])
            pos[1] += int(line[1]) * pos[2]
        elif line[0] == 'up':
            pos[2] -= int(line[1])
        elif line[0] == 'down':
            pos[2] += int(line[1])

print(f'Position. X = {pos[0]}, Y = {pos[1]}. Aim = {pos[2]}')
print(f'Internal product: {pos[0]} * {pos[1]} = {pos[0] * pos[1]}')