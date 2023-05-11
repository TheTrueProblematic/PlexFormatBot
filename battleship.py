import random

# Constants
BOARD_SIZE = 10

# Create a board filled with empty spaces
board = []
for i in range(BOARD_SIZE):
    row = []
    for j in range(BOARD_SIZE):
        row.append(' ')
    board.append(row)

import random

# Create an empty list
my_list = []

# Use a for loop to generate 10 random integers
# between 0 and 9 and append them to the list
for i in range(10):
  my_list.append((random.randint(0,9),random.randint(0,9)))

# Place the ships on the board
ships = my_list  # coordinates of ship cells
for x, y in ships:
    board[x][y] = ' '

# Show the board
print('   ' + ' '.join(str(i) for i in range(BOARD_SIZE)))
for i, row in enumerate(board):
    print(str(i) + ' ' + ' '.join(row))

# Play the game
while True:
    # Ask the player for a guess
    guess_x = int(input('Enter x coordinate: '))
    guess_y = int(input('Enter y coordinate: '))

    # Check if the guess is correct
    if board[guess_x][guess_y] == 'S':
        print('You hit a ship!')
        board[guess_x][guess_y] = 'H'
    else:
        print('You missed.')
        board[guess_x][guess_y] = 'X'

    # Check if all ships have been hit
    all_ships_hit = True
    for x, y in ships:
        if board[x][y] == 'S':
            all_ships_hit = False
            break
    if all_ships_hit:
        print('You sank all the ships! You win!')
        break

    # Show the board
    print('   ' + ' '.join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(str(i) + ' ' + ' '.join(row))