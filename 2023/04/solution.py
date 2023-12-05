with open("input.txt", "r") as f:
    # Get rid of card number, newline character and double spaces
    data = [line[line.index(":")+2:].strip().replace("  ", " ") for line in f.readlines()]
    # Split each line into a list of winning numbers and ticket numbers
    data = [line.split("|") for line in data]

points = []
for line in data:
    # Access winning numbers and ticket numbers
    winning_numbers = line[0].strip().split(" ")
    ticket_numbers = line[1].strip().split(" ")

    # Check if ticket numbers are in winning numbers
    count = 0 # Count of matching numbers
    for number in ticket_numbers:
        if number in winning_numbers:
            if count == 0:
                count += 1
            else:
                count *= 2

    # Add points to list
    points.append(count)

print("Part 1:", sum(points))
print("Part 2:", "No solution yet")