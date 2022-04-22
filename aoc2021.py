# ========================================= DAY 01 =========================================
def day1():
    part1, part2 = 0, 0

    with open("input_2021/day01.txt", "r") as f:
        data = f.readlines()

    previous_measurement = 0

    for index in range(len(data)):
        line = int(data[index])
        if 0 < previous_measurement < line:
            part1 += 1
        previous_measurement = line
    
    return part1, part2

# ================================== ADVENT OF CODE TABLE ==================================
if __name__ == "__main__":
    print(f"ADVENT OF CODE 2021")
    print(f"╔════════╦{'═' * 17}╦{'═' * 17}╗")
    print(f"║        ║ {'PART 1':>15} ║ {'PART 2':>15} ║")
    print(f"╠════════╬{'═' * 17}╬{'═' * 17}╣")
    print(f"║ DAY 01 ║ {day1()[0]:>15} ║ {day1()[1]:>15} ║")