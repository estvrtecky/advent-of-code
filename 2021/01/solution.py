part1, part2 = 0, 0

with open("input.txt", "r") as f:
    data = [int(line) for line in f]

for i in range(len(data)):
    if i >= 1 and data[i] > data[i-1]:
        part1 += 1
    if i >= 3 and data[i] + data[i-1] + data[i-2] > data[i-1] + data[i-2] + data[i-3]:
        part2 += 1

print("PART 1:", part1)
print("PART 2:", part2)