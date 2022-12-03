part1, part2 = 0, 0

with open('day02.txt', 'r') as f:
    data = [line.strip().split(' ') for line in f]

horizontal_position, depth_1, depth_2, aim = 0, 0, 0, 0
for command in data:
    direction, units = command[0], int(command[1])
    if direction == 'forward':
        horizontal_position += units
        depth_2 += aim * units
    elif direction == 'up':
        depth_1 -= units
        aim -= units
    elif direction == 'down':
        depth_1 += units
        aim += units

part1 = horizontal_position * depth_1
part2 = horizontal_position * depth_2

print('PART 1:', part1)
print('PART 2:', part2)