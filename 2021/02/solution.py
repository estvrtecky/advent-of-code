with open("input.txt", "r") as f:
    data = [line.strip().split(" ") for line in f.readlines()]

horizontal_pos = 0
depth_1, depth_2 = 0, 0
aim = 0

for command in data:
    direction, units = command[0], int(command[1])
    if direction == "forward":
        horizontal_pos += units
        depth_2 += aim * units
    elif direction == "up":
        depth_1 -= units
        aim -= units
    elif direction == "down":
        depth_1 += units
        aim += units

part1 = horizontal_pos * depth_1
part2 = horizontal_pos * depth_2

print("Part 1:", part1)
print("Part 2:", part2)