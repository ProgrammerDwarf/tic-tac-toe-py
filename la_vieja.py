from random import randrange

ROWS = 3
COLUMNS = 3
MAX_TURN = 9

PLAYER_SYMBOL = 'O'
COMPUTER_SYMBOL = 'X'

board = []
turn_counter = 1

def board_creation():
    cell_numbers = 1
    for rows in range(ROWS):
        rows_in_board = []
        for columns in range(COLUMNS):
            rows_in_board.append(cell_numbers)
            cell_numbers += 1
        board.append(rows_in_board)
    return board

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    separator = "+-------+-------+-------+"
    empty_lines = "|       |       |       |"
    for rows in board:
        print(separator)
        print(empty_lines)
        print("|",str(rows[0]).center(5),"|",str(rows[1]).center(5),"|",str(rows[2]).center(5),"|")
        print(empty_lines)
        print(separator, end='\r')

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_squares = make_list_of_free_fields(board)
    while True:
        try:
            user_move = int(input('Please, enter your move by entering a number between 1 and 9:\n'))
            
            if user_move < 1 or user_move > 9:
                print('Error: Number should be between 1 and 9. Enter it again, please!')
                continue
            
            row = (user_move - 1) // 3
            column = (user_move - 1) % 3
            
            if (row, column) in free_squares:
                board[row][column] = PLAYER_SYMBOL
                break
            else:
                print("Error: That square was already taken, please try another one!")
        except ValueError:
            print('Enter a number. Please, try again!')

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            if type(board[row_index][col_index]) == int:
                free_fields.append((row_index, col_index))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    victory_combinations = [
        [(0,0),(0,1),(0,2)],    # horizontal cond
        [(1,0),(1,1),(1,2)],    # horizontal cond
        [(2,0),(2,1),(2,2)],    # horizontal cond
        [(0,0),(1,0),(2,0)],    # vertical cond
        [(0,1),(1,1),(2,1)],    # vertical cond
        [(0,2),(1,2),(2,2)],    # vertical cond
        [(0,0),(1,1),(2,2)],    # diagonal cond
        [(2,0),(1,1),(0,2)],    # diagonal cond
        ]
    for conditions in victory_combinations:
        symbol_counter = 0
        for cell in conditions:
            row, column = cell
            if board[row][column] == sign:
                symbol_counter += 1
                if symbol_counter == 3:
                    return True

def draw_move(board):
        empty_fields = make_list_of_free_fields(board)
        field_to_fill = randrange(len(empty_fields))
        row_to_fill, column_to_fill = empty_fields[field_to_fill]
        board[row_to_fill][column_to_fill] = COMPUTER_SYMBOL
        return board

#Empiezo del flujo 
board_creation()

board[1][1] = COMPUTER_SYMBOL
display_board(board)

turn_counter += 1

while True:
    if turn_counter % 2 == 0:
        print('\nPlayer\'s turn!\n')
        enter_move(board)
        display_board(board)
        if victory_for(board, PLAYER_SYMBOL):
            print('\nHuman wins')
            break
    else:
        print('\nComputer\'s turn!\n')
        draw_move(board)
        display_board(board)
        if victory_for(board, COMPUTER_SYMBOL):
            print('\nComputer wins')
            break
    
    if len(make_list_of_free_fields(board)) == 0:
        print('\nTied game')
        break
    
    turn_counter += 1