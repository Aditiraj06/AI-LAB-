import random

board = [" "] * 9
game_active = True


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_win(player):
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for line in winning_lines:
        if all(board[position] == player for position in line):
            return True

    return False


def check_tie():
    return " " not in board


def computer_move():
    empty_spaces = []

    for i in range(9):
        if board[i] == " ":
            empty_spaces.append(i)

    if empty_spaces:
        move = random.choice(empty_spaces)
        board[move] = "O"

while game_active:

    print_board()

    try:
        move = int(input("Your move (0-8): "))
    except ValueError:
        print("Invalid move. Please enter a number from 0 to 8.")
        continue

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move. Try again.")
        continue

    board[move] = "X"

    if check_win("X"):
        print_board()
        print("You win!")
        break

    if check_tie():
        print_board()
        print("Tie game!")
        break

    computer_move()

    print("Computer chose a move.")

    if check_win("O"):
        print_board()
        print("Computer wins!")
        break

    if check_tie():
        print_board()
        print("Tie game!")
        break