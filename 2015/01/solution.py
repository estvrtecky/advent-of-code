floor, position = 0, 0

with open("input.txt", "r") as f:
    data = f.read()

for index, char in enumerate(data):
    # Part1 - find the floor Santa ends up on
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

    # Part2 - find the position of the first character that causes him to enter the basement
    if floor == -1 and position == 0:
        position = index + 1

print("Part 1:", floor)
print("Part 2:", position)