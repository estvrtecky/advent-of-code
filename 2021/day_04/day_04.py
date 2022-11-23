part1, part2 = 0, 0

with open('day_04_input.txt', 'r') as f:
    nums, *boards = f.read().split('\n\n')
    nums = nums.split(',')
    boards = [[[num for num in row.split()] for row in board.split('\n')] for board in boards]

def mark_num(num):
    for board in boards:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == num:
                    board[row][col] = 'X'

def check_board(board):
    for row in board:
        if all(num == 'X' for num in row):
            return True
    for col in range(len(board[0])):
        if all(num == 'X' for num in [row[col] for row in board]):
            return True

def score(multiply_num, board):
    sum_unmarked = 0
    for row in board:
        for num in row:
            if num != 'X': sum_unmarked += int(num)
    return sum_unmarked * int(multiply_num)

first = True
stop = False
for num in nums:
    for i, board in enumerate(boards):
        mark_num(num)
        if len(boards) > 1:
            if check_board(board):
                if first:
                    part1 = score(num, board)
                    first = False
                boards.pop(i)
        else:
            print(board)
            part2 = score(num, board)
            stop = True
    if stop: break

print('PART 1:', part1)
print('PART 2:', part2)