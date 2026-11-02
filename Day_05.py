# 8 Queen 
n = 8
board = [-1] * n

for row in range(n):
    for col in range(n):
        safe = True

        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                safe = False
                break

        if safe:
            board[row] = col
            break

print("8 Queens Solution:")
for i in range(n):
    for j in range(n):
        if board[i] == j:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
