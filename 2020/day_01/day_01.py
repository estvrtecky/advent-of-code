part1, part2 = 0, 0

with open('day_01_input.txt', 'r') as f:
    data = [int(line) for line in f]

for num1 in data:
    for num2 in data:
        if num1 + num2 == 2020:
            part1 = num1 * num2
        if part2 == 0:
            for num3 in data:
                if num1 + num2 + num3 == 2020:
                    part2 = num1 * num2 * num3

print('PART 1:', part1)
print('PART 2:', part2)