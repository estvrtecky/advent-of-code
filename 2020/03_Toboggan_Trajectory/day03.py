part1, part2 = 0, 1

with open('day03.txt', 'r') as f:
    data = [line.strip() for line in f]

def collisions(right, down):
    trees = 0
    x, y = 0, 0
    while True:
        y += down
        x = (x + right) % len(data[0])
        if y >= len(data): break
        if data[y][x] == '#': trees += 1
    return trees

part1 = collisions(3, 1)
for i in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    part2 *= collisions(i[0], i[1])

print('PART 1:', part1)
print('PART 2:', part2)