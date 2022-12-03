part1, part2 = 0, 0

with open('day01.txt', 'r') as f:
    data = [int(line) for line in f]

for num1 in data:
    for num2 in data:
        if num1 + num2 == 2020:
            part1 = num1 * num2
        if 2020 - num1 - num2 in data:
            part2 = num1 * num2 * (2020 - num1 - num2)

print('PART 1:', part1)
print('PART 2:', part2)