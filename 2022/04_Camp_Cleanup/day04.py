part1, part2 = 0, 0

with open('day04.txt', 'r') as f:
    pairs = [pair.strip().split(',') for pair in f.readlines()]

for pair in pairs:
    elf1, elf2 = pair[0].split('-'), pair[1].split('-')
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        part1 += 1
    elif int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
        part1 += 1
    if not (int(elf1[1]) < int(elf2[0]) or int(elf2[1]) < int(elf1[0])):
        part2 += 1

print('PART 1:', part1)
print('PART 2:', part2)