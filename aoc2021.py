# ========================================= DAY 01 =========================================
def day1():
    part1, part2 = 0, 0

    with open("input_2021/day01.txt", "r") as f:
        data = [int(line.strip()) for line in f]

    for index in range(len(data)):
        if index >= 1 and data[index] > data[index - 1]:
            part1 += 1
        if index >= 3 and data[index] + data[index - 1] + data[index - 2] > data[index - 1] + data[index - 2] + data[index - 3]:
            part2 += 1

    return part1, part2

# ========================================= DAY 02 =========================================
def day2():
    part1, part2 = 0, 0

    with open("input_2021/day02.txt", "r") as f:
        data = [line.strip() for line in f]

    horizontal_position = 0
    depth = 0

    for line in data:
        command, number = line.split()
        if command == "forward":
            horizontal_position += int(number)
        elif command == "up":
            depth -= int(number)
        elif command == "down":
            depth += int(number)
    
    part1 = horizontal_position * depth

    return part1, part2

# ================================== ADVENT OF CODE TABLE ==================================
if __name__ == "__main__":
    print(f"ADVENT OF CODE 2021")
    print(f"╔════════╦{'═' * 17}╦{'═' * 17}╗")
    print(f"║        ║ {'PART 1':>15} ║ {'PART 2':>15} ║")
    print(f"╠════════╬{'═' * 17}╬{'═' * 17}╣")
    print(f"║ DAY 01 ║ {day1()[0]:>15} ║ {day1()[1]:>15} ║")
    print(f"║ DAY 02 ║ {day2()[0]:>15} ║ {day2()[1]:>15} ║")