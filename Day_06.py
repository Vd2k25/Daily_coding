board = [" " for i in range(9)]
print("TIC TAC TOE")
print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")
player = "X"

for i in range(9):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

    position = int(input("Player " + player + ", enter position (1-9): "))

    if position < 1 or position > 9 or board[position - 1] != " ":
        print("Invalid position! Try again.")
        continue

    board[position - 1] = player

    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player or
        board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player or
        board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):

        print("\n")
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])

        print("Player", player, "wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    print("Match Draw!")
