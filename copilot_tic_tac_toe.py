def print_board(game_board):
    """
    Prints a visual representation of a board in the form of
    game_board = [0, 1, 2, 3, 4, 5,6, 7, 8]
    """
    print("\n")
    print("\t", game_board[0], "|", game_board[1], "|", game_board[2])
    print("\t", "---------")
    print("\t", game_board[3], "|", game_board[4], "|", game_board[5])
    print("\t", "---------")
    print("\t", game_board[6], "|", game_board[7], "|", game_board[8])
    print("\n")


def player_turn(game_board, player):
    """
    Asks the player for a move and updates the game_board
    """
    player_move = int(input("Where would you like to move? "))
    game_board[player_move] = player
    return game_board


def check_win(game_board, player):
    """
    Checks to see if the player has won the game.
    """
    if game_board[0] == player and game_board[1] == player and game_board[2] == player:
        return True
    elif (
        game_board[3] == player and game_board[4] == player and game_board[5] == player
    ):
        return True
    elif (
        game_board[6] == player and game_board[7] == player and game_board[8] == player
    ):
        return True
    elif (
        game_board[0] == player and game_board[3] == player and game_board[6] == player
    ):
        return True
    elif (
        game_board[1] == player and game_board[4] == player and game_board[7] == player
    ):
        return True
    elif (
        game_board[2] == player and game_board[5] == player and game_board[8] == player
    ):
        return True
    elif (
        game_board[0] == player and game_board[4] == player and game_board[8] == player
    ):
        return True
    elif (
        game_board[2] == player and game_board[4] == player and game_board[6] == player
    ):
        return True
    else:
        return False


def check_tie(game_board):
    """
    Checks to see if the game is a tie.
    """
    if "" not in game_board:
        return True
    else:
        return False


def tic_tac_toe():
    """
    Create a working Tic Tac Toe game.
    The game should be able to be played on a terminal or a GUI.
    The game should be able to be played by two human players or one human player and one computer player.
    """
    print("Welcome to Tic Tac Toe!")
    print("To play, you will need to enter a number between 1 and 9.")
    print("The numbers will correspond to the following positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("The first player to get three in a row wins!")
    print("Enter 'q' to quit the game.")
    print("Let's get started!")
    print("\n")

    # Create game board
    game_board = ["", "", "", "", "", "", "", "", ""]

    player1 = "X"
    player2 = "O"

    # Game loop
    while True:
        print_board(game_board)
        game_board = player_turn(game_board, player1)
        print_board(game_board)
        if check_win(game_board, player1):
            print("Player 1 wins!")
            break
        elif check_tie(game_board):
            print("It's a tie!")
            break
        game_board = player_turn(game_board, player2)
        print_board(game_board)
        if check_win(game_board, player2):
            print("Player 2 wins!")
            break
        elif check_tie(game_board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    tic_tac_toe()
