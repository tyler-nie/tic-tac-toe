board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def draw():
    # Draws the board

    print(board[6] + "|" + board[7] + "|" + board[8])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[0] + "|" + board[1] + "|" + board[2])


def full_board_detection():
    # Detects if there are anymore spaces

    full = True
    for space in board:
        # Detects if there are empty spaces on the board
        if space == " ":
            full = False
    return full


def winner():
    # Detects if there is winner

    win = False
    if board[0] == board[1] and board[1] == board[2] and board[0] != " ":
        win = True
    if board[3] == board[4] and board[4] == board[5] and board[3] != " ":
        win = True
    if board[6] == board[7] and board[7] == board[8] and board[6] != " ":
        win = True
    if board[0] == board[3] and board[3] == board[6] and board[0] != " ":
        win = True
    if board[1] == board[4] and board[4] == board[7] and board[1] != " ":
        win = True
    if board[2] == board[5] and board[5] == board[8] and board[2] != " ":
        win = True
    if board[0] == board[4] and board[4] == board[8] and board[8] != " ":
        win = True
    if board[2] == board[4] and board[4] == board[6] and board[6] != " ":
        win = True
    return win


draw()


while True:
    # Player one's turn
    while True:
        try:
            player_one = int(input("X's turn: "))

            if player_one < 1 or player_one > 9:
                print("Not valid position")
            elif board[player_one - 1] != " ":
                print("That position is taken")
            else:
                break
        except ValueError:
            print("Not a valid number")

    board[player_one - 1] = "X"
    draw()

    if winner():
        print("X Wins!")
        break

    if full_board_detection():
        break

    # Player two's turn
    while True:
        try:
            player_two = int(input("O's turn: "))

            if player_two < 1 or player_two > 9:
                print("Not valid position")
            elif board[player_two - 1] != " ":
                print("That position is taken")
            else:
                break
        except ValueError:
            print("Not a valid number")

    board[player_two - 1] = "O"
    draw()

    if winner():
        print("O Wins!")
        break

    if full_board_detection():
        break

print("Game Over")
