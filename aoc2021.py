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
    part1, part2 = 0, 0





# ================================== ADVENT OF CODE TABLE ==================================
if __name__ == "__main__":
    print(f"ADVENT OF CODE 2021")
    print(f"╔════════╦{'═' * 17}╦{'═' * 17}╗")
    print(f"║        ║ {'PART 1':>15} ║ {'PART 2':>15} ║")
    print(f"╠════════╬{'═' * 17}╬{'═' * 17}╣")
    print(day_02())
