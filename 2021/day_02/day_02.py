part1, part2 = 0, 0

with open('day_02_input.txt', 'r') as f:
    data = [line.strip() for line in f]

horizontal_position, depth_1, depth_2, aim = 0, 0, 0, 0
for command in data:
    direction, units = command.split(' ')[0], int(command.split(' ')[1])
    if direction == 'forward':
        horizontal_position += units
        depth_2 += aim * units
    elif direction == 'up':
        depth_1 -= units
        aim -= units
    elif direction == 'down':
        depth_1 += units
        aim += units

print('PART 1:', horizontal_position * depth_1)
print('PART 2:', horizontal_position * depth_2)