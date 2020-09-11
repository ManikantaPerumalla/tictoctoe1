print("play the game: tic toc toe")
#board
#handle player
#flip player
#check for Win
#check rows
#check coloumns
#check diagonals

#check for tie

#creating board stuff
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
# if game is still game_is_running
game_is_running = True

#who won
winner = None

#who's turn
current_player = "s"


#creating board
def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    #showing board
    show_board()
    #to handle the player
    while game_is_running:
        # to handle the pkayer
        handle_player(current_player)
        #to check the game is over or Not

        check_if_game_over()

        #to change the move of player

        flip_player()

        #check for winner
        if winner == "s" or winner == "m":
            print(winner + "   won...")
    else:
        print("tie.....")


def handle_player(player):
    print(player + " 's turn")
    position = input("enter a number from 1-9......    ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("invalid input.enter a number from 1-9......  ")
    position = int(position) - 1
    if board[position] != "-":
        print("you can't go there")
    board[position] = player
    show_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    #global variables
    global row_winner
    global coloumn_winner
    global diagonal_winner
    global winner

    #check rows
    row_winner = check_rows()
    #check coloumns
    coloumn_winner = check_coloumns()
    #check diagonals
    diagonal_winner = check_diagonal()
    if row_winner:
        #win
        winner = row_winner
    elif coloumn_winner:
        #win
        winner = coloumn_winner
    elif diagonal_winner:
        #winn
        winner = diagonal_winner

    return


def check_rows():
    #set global variables
    global game_is_running
    #row1
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        game_is_running = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_coloumns():
    #set global variables
    global game_is_running
    #row1
    col1 = board[0] == board[3] == board[6] != "_"
    col2 = board[1] == board[4] == board[7] != "_"
    col3 = board[2] == board[5] == board[8] != "_"
    if col1 or col2 or col3:
        game_is_running = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return
    return


def check_diagonal():
    #set global variables
    global game_is_running
    #row1
    dig1 = board[0] == board[4] == board[8] != "_"
    dig2 = board[2] == board[4] == board[6] != "_"

    if dig1 or dig2:
        game_is_running = False
    if dig1:
        return board[0]
    elif dig2:
        return board[2]
    return


def check_if_tie():
    global game_is_running
    if "_" not in board:
        game_is_running = False
        return
    return


def flip_player():
    global current_player
    if current_player == "s":
        current_player = "m"
        return
    elif current_player == "m":
        current_player = "s"
        return
    return


play_game()
