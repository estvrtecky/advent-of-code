part1, part2 = 0, 0

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

for line in data:
    digits1 = [char for char in line if char.isdigit()]
    digits2 = []
    for i, char in enumerate(line):
        if char.isdigit():
            digits2.append(char)
        for num, word in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if line[i:].startswith(word):
                digits2.append(str(num + 1))
    part1 += int(digits1[0] + digits1[-1])
    part2 += int(digits2[0] + digits2[-1])

print("Part 1:", part1)
print("Part 2:", part2)