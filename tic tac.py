#Tic tac game

#game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# Variables
playing = True

player = "X"



def play_game():
    while playing:
        display_board()
        player_turn(player)
        switch_player()
        check_winner()
        check_tie()




def display_board():
#display the  game board for tic tac toe
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def player_turn(player):
#player decides where to place his next move

    movement = input("Please choose 1-9: ")
    while movement != ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("try again")
        player_turn(player)
        movement = int(movement) -1
    if board[movement] == "-":
        board[movement] = player
    elif board[movement] != "-" and not "X" or "O":
        print("You cannot go there! Try again ")
        player_turn(player)







def switch_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

def check_winner():
    #check if a playing has been made
    row_winner()
    column_winner()
    diagonal_winner()


def row_winner():
#check whether a row has a playing
    global playing
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        display_board()
        switch_player()  #switch player to show the correct winner
        print(player + "won!")
        playing = False


def column_winner():
#check whether a column has a playing
    global playing
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        display_board()
        switch_player()  #switch player to show the correct winner
        print(player + "won!")
        playing = False


def diagonal_winner():
#check whether a diagonal has a playing
    global playing
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        display_board()
        switch_player()  #switch player to show the correct winner
        print(player + "won!")
        playing = False

def check_tie():
    global playing
    if "-" not in board:
        display_board()
        playing = False
        print("tie!")




play_game()



