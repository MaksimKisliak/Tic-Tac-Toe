import random


def print_board(board):
    """
    Print the Tic Tac Toe board
    """
    for row in board:
        print("|".join(row))


def check_winner(board):
    """
    Check if there is a winner on the board
    """
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]

        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    return None


def get_player_move(board):
    """
    Get the player's move and validate it
    """
    while True:
        move = input("Enter your move in the format row,col (e.g. 1,2): ")

        try:
            row, col = map(int, move.split(","))
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid move. Please enter a value between 1 and 3 for both row and column.")
            elif board[row - 1][col - 1] != "-":
                print("That space is already occupied. Please choose another space.")
            else:
                return row - 1, col - 1
        except ValueError:
            print("Invalid move. Please enter your move in the format row,col (e.g. 1,2).")


def get_computer_move(board):
    """
    Get the computer's move
    """
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == "-"]
    if not available_moves:
        return None
    return random.choice(available_moves)


def play_game():
    """
    Play a game of Tic Tac Toe
    """
    print("Welcome to Tic Tac Toe!")
    board = [["-" for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # Player's move
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = "X"
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break

        # Computer's move
        print("The computer is thinking...")
        computer_move = get_computer_move(board)
        if computer_move is None:
            print("It's a tie!")
            break
        computer_row, computer_col = computer_move
        board[computer_row][computer_col] = "O"
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break


if __name__ == "__main__":
    play_game()
