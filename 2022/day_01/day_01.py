part1, part2 = 0, 0

with open('day_01_input.txt', 'r') as f:
    data = f.read().split('\n\n')
    elves = [elf.split('\n') for elf in data]
    calories = sorted([sum([int(item) for item in elf]) for elf in elves], reverse=True)

part1 = calories[0]
part2 = sum(calories[:3])

print('PART 1:', part1)
print('PART 2:', part2)