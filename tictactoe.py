# write your code here
movs = "_________"
movs2 = [movs[0:3], movs[3:6], movs[6:9]]
print("---------")
for s in movs2:
    print("|", *s, "|")
print("---------")

row_winX = None
row_winO = None
col_winO = None
col_winX = None
diag_winX = None
diag_winO = None
winner = any([row_winX, row_winO, col_winX, col_winO, diag_winX, diag_winO])

def indice(x, y):
    indx = (x - 1) + (9 - (3 * y))
    return indx


def check_result(matrix, moves):
    # check rows
    global row_winX
    global col_winX
    global diag_winX
    global row_winO
    global col_winO
    global diag_winO
    global winner
    col1 = [sub[0] for sub in matrix]
    col2 = [sub[1] for sub in matrix]
    col3 = [sub[2] for sub in matrix]
    columns = [col1, col2, col3]
    diag1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    diag2 = [matrix[0][2], matrix[1][1], matrix[2][0]]

    for i in matrix:
        if i.count("O") == 3 and i.count("X") == 3:
            print("Impossible")
        elif i.count("X") == 3:
            row_winX = True
            print("X wins")
            winner = True
        elif i.count("O") == 3:
            row_winO = True
            print("O wins")
            winner = True

    if diag1.count("X") == 3 or diag2.count("X") == 3:
        print("X wins")
        diag_winX = True
        winner = True
    elif diag1.count("O") == 3 or diag2.count("O") == 3:
        print("O wins")
        diag_winO = True
        winner = True

    # check columns
    for c in columns:
        if c.count("O") == 3:
            col_winO = True
            winner = True
        if c.count("X") == 3:
            col_winX = True
            winner = True
    if col_winX is True and col_winO is True:
        print("Impossible")
    elif col_winO is True:
        print("O wins")
    elif col_winX is True:
        print("X wins")

    # Draw/impossible and not finished
    if row_winX is not True and col_winX is not True and diag_winX is not True and row_winO is not True and col_winO is not True and diag_winO is not True:
        if moves.count("X") > (moves.count("O") + 1) or moves.count("O") > (moves.count("X") + 1):
            print("Impossible")
        elif moves.count("_") == 0:
            print("Draw")
            winner = True
        elif moves.count("_") > 0:
            print("Game not finished")
    elif moves.count("X") > (moves.count("O") + 1) or moves.count("O") > (moves.count("X") + 1):
        print("Impossible")
    return winner


#get and check coordinates
while winner is False:
    while True:
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
            while x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
                x, y = map(int, input("Enter the coordinates: ").split())
            else:
                i = indice(x, y)
                while movs[i] == "X" or movs[i] == "O":
                    print("This cell is occupied! Choose another one!")
                    x, y = map(int, input("Enter the coordinates: ").split())
                    i = indice(x, y)
            break
        except ValueError:
            print("You should enter numbers!")

#index again for new matrix. For efficiency, this should be improved, since the value is in the loop
    i = indice(x, y)

# new matrix
    movs = movs[:i] + "X" + movs[i + 1:]
    movs2 = [movs[0:3], movs[3:6], movs[6:9]]
    print("---------")
    for s in movs2:
        print("|", *s, "|")
    print("---------")
    check_result(movs2, movs)
    if winner is True:
        break

    while True:
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
            while x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
                x, y = map(int, input("Enter the coordinates: ").split())
            else:
                i = indice(x, y)
                while movs[i] == "X" or movs[i] == "O":
                    print("This cell is occupied! Choose another one!")
                    x, y = map(int, input("Enter the coordinates: ").split())
                    i = indice(x, y)
            break
        except ValueError:
            print("You should enter numbers!")

    movs = movs[:i] + "O" + movs[i + 1:]
    movs2 = [movs[0:3], movs[3:6], movs[6:9]]
    print("---------")
    for s in movs2:
        print("|", *s, "|")
    print("---------")

    check_result(movs2, movs)
    if winner is True:
        break





