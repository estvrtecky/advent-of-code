part1, part2 = 0, 0

with open("input.txt", "r") as f:
    elves = [elf.split("\n") for elf in f.read().split("\n\n")]
    calories = sorted([sum([int(item) for item in elf]) for elf in elves], reverse=True)

part1 = calories[0]
part2 = sum(calories[:3])

print("Part 1:", part1)
print("Part 2:", part2)