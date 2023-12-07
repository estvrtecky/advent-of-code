part1, part2 = 0, 0

with open("input.txt", "r") as f:
    data = [line.strip().split("x") for line in f.readlines()]

for line in data:
    l = int(line[0])
    w = int(line[1])
    h = int(line[2])
    area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l) # Smallest side
    part1 += area + slack
    part2 += 2*min(l+w, w+h, h+l) + l*w*h

print("Part 1:", part1)
print("Part 2:", part2)