# ========================================= DAY 01 =========================================
def day_01():
    part1, part2 = 0, 0

    with open("input_2021/day_01.txt", "r") as f:
        data = [int(line.strip()) for line in f]

    for i in range(len(data)):
        if i >= 1 and data[i] > data[i-1]:
            part1 += 1
        if i >= 3 and data[i] + data[i-1] + data[i-2] > data[i-1] + data[i-2] + data[i-3]:
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

# ========================================= DAY 03 =========================================
def day_03():
    part1, part2 = 0, 0

    with open("input_2021/day_03.txt", "r") as f:
        data = [str(line.strip()) for line in f]

    gamma, epsilon = "", ""

    for bit in range(len(data[0])):
        bits_at_pos = [binary[bit] for binary in data]
        if bits_at_pos.count("0") > bits_at_pos.count("1"):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    oxygen_rating, co2_rating = "", ""
    oxygen_data, co2_data = data.copy(), data.copy()

    for bit in range(len(oxygen_data[0])):
        if len(oxygen_data) == 1:
            oxygen_rating = oxygen_data[0]
            break
        bits_at_pos = [binary[bit] for binary in oxygen_data]
        if bits_at_pos.count("0") <= bits_at_pos.count("1"):
            oxygen_rating += "1"
        else:
            oxygen_rating += "0"
        _ = []
        for binary in oxygen_data:
            if binary[len(oxygen_rating)-1] == oxygen_rating[-1]:
                _.append(binary)
        oxygen_data = _

    for bit in range(len(co2_data[0])):
        if len(co2_data) == 1:
            co2_rating = co2_data[0]
            break
        bits_at_pos = [binary[bit] for binary in co2_data]
        if bits_at_pos.count("0") > bits_at_pos.count("1"):
            co2_rating += "1"
        else:
            co2_rating += "0"
        _ = []
        for binary in co2_data:
            if binary[len(co2_rating)-1] == co2_rating[-1]:
                _.append(binary)
        co2_data = _

    part1 = int(gamma, 2) * int(epsilon, 2)
    part2 = int(oxygen_rating, 2) * int(co2_rating, 2)

    return f"║ DAY 03 ║ {part1:>15} ║ {part2:>15} ║"

# ================================== ADVENT OF CODE TABLE ==================================
if __name__ == "__main__":
    print(f"ADVENT OF CODE 2021")
    print(f"╔════════╦{'═' * 17}╦{'═' * 17}╗")
    print(f"║        ║ {'PART 1':<15} ║ {'PART 2':<15} ║")
    print(f"╠════════╬{'═' * 17}╬{'═' * 17}╣")
    print(day_01())
    print(day_02())
    print(day_03())