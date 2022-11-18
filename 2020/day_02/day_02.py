part1, part2 = 0, 0

with open('day_02_input.txt', 'r') as f:
    data = [line.strip() for line in f]

for line in data:
    num, letter, password = line.split(' ')
    l_num, h_num = num.split('-')
    letter = letter[0]
    if int(l_num) <= password.count(letter) <= int(h_num):
        part1 += 1
    if (password[int(l_num)-1] == letter) ^ (password[int(h_num)-1] == letter):
        part2 += 1

print('PART 1:', part1)
print('PART 2:', part2)