part1, part2 = 0, 0

with open('day_03_input.txt', 'r') as f:
    data = [line.strip() for line in f]

gamma, epsilon = '', ''

for bit in range(len(data[0])):
    bits_at_pos = [binary[bit] for binary in data]
    if bits_at_pos.count('0') > bits_at_pos.count('1'):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

oxygen_rating, co2_rating = '', ''
oxygen_data, co2_data = data.copy(), data.copy()

for bit in range(len(oxygen_data[0])):
    if len(oxygen_data) == 1:
        oxygen_rating = oxygen_data[0]
        break
    bits_at_pos = [binary[bit] for binary in oxygen_data]
    if bits_at_pos.count('0') <= bits_at_pos.count('1'):
        oxygen_rating += '1'
    else:
        oxygen_rating += '0'
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
    if bits_at_pos.count('0') > bits_at_pos.count('1'):
        co2_rating += '1'
    else:
        co2_rating += '0'
    _ = []
    for binary in co2_data:
        if binary[len(co2_rating)-1] == co2_rating[-1]:
            _.append(binary)
    co2_data = _

part1 = int(gamma, 2) * int(epsilon, 2)
part2 = int(oxygen_rating, 2) * int(co2_rating, 2)

print('PART 1:', part1)
print('PART 2:', part2)