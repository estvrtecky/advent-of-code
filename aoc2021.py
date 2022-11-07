# ========================================= DAY 01 =========================================
def day_01():
    part1, part2 = 0, 0

    with open("input_2021/day_01.txt", "r") as f:
        data = [int(line.strip()) for line in f]

    for index in range(len(data)):
        if index >= 1 and data[index] > data[index - 1]:
            part1 += 1
        if index >= 3 and data[index] + data[index - 1] + data[index - 2] > data[index - 1] + data[index - 2] + data[index - 3]:
            part2 += 1

    return f"║ DAY 01 ║ {part1:>15} ║ {part2:>15} ║"

# ========================================= DAY 02 =========================================
def day_02():
    part1, part2 = 0, 0

    with open("input_2021/day_02.txt", "r") as f:
        data = [str(line.strip()) for line in f]

    horizontal_position, depth_1, depth_2, aim = 0, 0, 0, 0

    for command in data:
        direction, units = command.split(" ")[0], int(command.split(" ")[1])
        if direction == "forward":
            horizontal_position += units
            depth_2 += aim * units
        elif direction == "up":
            depth_1 -= units
            aim -= units
        elif direction == "down":
            depth_1 += units
            aim += units

    part1 = horizontal_position * depth_1
    part2 = horizontal_position * depth_2

    return f"║ DAY 02 ║ {part1:>15} ║ {part2:>15} ║"





# ================================== ADVENT OF CODE TABLE ==================================
if __name__ == "__main__":
    print(f"ADVENT OF CODE 2021")
    print(f"╔════════╦{'═' * 17}╦{'═' * 17}╗")
    print(f"║        ║ {'PART 1':>15} ║ {'PART 2':>15} ║")
    print(f"╠════════╬{'═' * 17}╬{'═' * 17}╣")
    print(day_01())
    print(day_02())
