part1, part2 = 0, 0

with open("input.txt", "r") as f:
    data = f.read()

# Part 1
# set of coordinates of houses that have received at least one present
houses = set((0, 0)) # start at (0, 0)

x, y = 0, 0
for char in data:
    if char == "^":
        y += 1
    elif char == "v":
        y -= 1
    elif char == ">":
        x += 1
    elif char == "<":
        x -= 1
    houses.add((x, y))

part1 = len(houses) # number of houses that have received at least one present

print("Part 1:", part1)
print("Part 2:", part2)