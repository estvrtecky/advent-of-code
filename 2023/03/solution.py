part1, part2 = 0, 0

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

def check_symbol(x, y):
    for rowIndex in range(-1, 2):
        for colIndex in range(-1, 2):
            if rowIndex == 0 and colIndex == 0:
                continue

            if 0 <= (x + colIndex) < len(data[0]) and 0 <= (y + rowIndex) < len(data) and data[y + rowIndex][x + colIndex] not in "1234567890.":
                return True


for rowIndex, line in enumerate(data):
    number = ""
    symbol = False
    for colIndex, char in enumerate(line):
        if char.isdigit():
            number += char
            if not symbol:
                symbol = check_symbol(colIndex, rowIndex)
        else:
            if symbol:
                part1 += int(number)
                symbol = False
            number = ""
    if symbol:
        part1 += int(number)
        symbol = False
    number = ""


print("Part 1:", part1)
print("Part 2:", part2)