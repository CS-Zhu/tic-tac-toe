"""
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
"""
board = {
    "1": "1", "2": "2", "3": "3",
    "4": "4", "5": "5", "6": "6",
    "7": "7", "8": "8", "9": "9"
}

def print_board(board):
    print(board["1"] + " | " + board["2"] + " | " + board["3"])
    print("---------")
    print(board["4"] + " | " + board["5"] + " | " + board["6"])
    print("---------")
    print(board["7"] + " | " + board["8"] + " | " + board["9"])

def check_position(user_input):
    marked = ['x', 'o']
    for key in board.keys():
        if key == user_input:
            if board[key] not in marked:
                return True
            return False

def marked_board(position, symbol):
    board[position] = symbol
    
def check_input(user_input):
    # check if input is 1 to 9
    valid_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if user_input in valid_input:
        if check_position(user_input):
            return True
        else:
            print("Position already marked")
    else:
        print("invalid posiiton")
        return False

def winning_check():
    # check horizontal
    if board['1'] == board['2'] and board['1'] == board['3']:
        return True
    if board['4'] == board['5'] and board['4'] == board['6']:
        return True
    if board['7'] == board['8'] and board['7'] == board['9']:
        return True
    # check vertical
    if board['1'] == board['4'] and board['1'] == board['7']:
        return True
    if board['2'] == board['5'] and board['2'] == board['8']:
        return True
    if board['3'] == board['6'] and board['3'] == board['9']:
        return True
    # check diagonal
    if board['1'] == board['5'] and board['1'] == board['9']:
        return True
    if board['3'] == board['5'] and board['3'] == board['7']:
        return True

if __name__ == "__main__":
    valid_symbol = ['x', 'o']
    user1_symbol = ''
    user2_symbol = 'x'
    while True:
        user1_symbol = input("Player1, please Choose a symbol from \"x\" and \"o\"\n")
        if user1_symbol in valid_symbol:
            break
        print("Please choose a valid symbol")
    if user1_symbol == 'x':
        user2_symbol = 'o'
    print("Player 1 will use {}".format(user1_symbol))
    print("Player 2 will use {}".format(user2_symbol))
    print("############################")
    print("###    Start Game !!!    ###")
    print("############################")
    print_board(board)

    while True:
        user1_input = input("Player1, lease enter a position number or entry \"q\" to quit:\n")
        
        if user1_input == 'q':
            break
        
        while not check_input(user1_input):
            user1_input = input("Player1, lease enter a position number or entry \"q\" to quit:\n")
                
        marked_board(user1_input, user1_symbol)
        print_board(board)
        if winning_check():
            print("Congradulations!!!!! Player1 You Have Won the Game")
            break
    
        user2_input = input("Player2, lease enter a position number or entry \"q\" to quit:\n")
        if user2_input == 'q':
            break
        
        while not check_input(user2_input):
            user2_input = input("Player2, lease enter a position number or entry \"q\" to quit:\n")
                
        marked_board(user2_input, user2_symbol)
        print_board(board)
        if winning_check():
            print("Congradulations!!!!! Player2 You Have Won the Game")
            break
    