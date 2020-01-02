print("\n                         ***This is Sudoku Cracker Program***")
print("\nIt can crack 4x4, 6x6, 8x8, 9x9, 10x10, 12x12, 15x15, 16x16, 25x25 sudoku problems")
print("Note : - Empty spaces are shown by zero(0)\n\n")
rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))

print("Enter the entries row-wise separated by space (Hit enter after inputting each row):\n ") 
sudoku_board = [[0]*columns for _ in range(rows)]
for i in range(columns):
    sudoku_board[i] = [int(j) for j in input().strip().split(" ")]


def sudokusolver(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find[0],find[1]

    for i in range(1,rows+1):
        if valid(board, i,row, col):
            board[row][col] = i

            if sudokusolver(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, row,col):
    # checks row for same number
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    # Checks column for same number
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check box
    if(rows == 4 and columns == 4):
        boxRow = col // 2
        boxColumn = row // 2
        for i in range( boxColumn*2,  boxColumn*2 + 2):
            for j in range(boxRow * 2, boxRow*2 + 2):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False
        
    elif(rows == 6 and columns == 6):
        boxRow = col //3
        boxColumn = row //2
        for i in range( boxColumn*2,  boxColumn*2 + 2):
            for j in range(boxRow * 3, boxRow*3 + 3):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False

    elif(rows == 8 and columns == 8):
        boxRow = col //4
        boxColumn = row //2
        for i in range( boxColumn*2,  boxColumn*2 + 2):
            for j in range(boxRow * 4, boxRow*4 + 4):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False

    elif(rows == 9 and columns == 9):
        boxRow = col //3
        boxColumn = row //3
        for i in range( boxColumn*3,  boxColumn*3 + 3):
            for j in range(boxRow * 3, boxRow*3 + 3):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False

    elif(rows == 10 and columns == 10):
        boxRow = col //5
        boxColumn = row //2
        for i in range( boxColumn*2,  boxColumn*2 + 2):
            for j in range(boxRow * 5, boxRow*5 + 5):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False

    elif(rows == 12 and columns == 12):
        boxRow = col //6
        boxColumn = row //2
        for i in range( boxColumn*2,  boxColumn*2 + 2):
            for j in range(boxRow * 6, boxRow*6 + 6):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False
        
    elif(rows == 15 and columns == 15):
        boxRow = col //5
        boxColumn = row //3
        for i in range( boxColumn*3,  boxColumn*3 + 3):
            for j in range(boxRow * 5, boxRow*5 + 5):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False

    elif(rows == 16 and columns == 16):
        boxRow = col //4
        boxColumn = row //4
        for i in range( boxColumn*4,  boxColumn*4 + 4):
            for j in range(boxRow * 4, boxRow*4 + 4):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False

    elif(rows == 25 and columns == 25):
        boxRow = col //5
        boxColumn = row //5
        for i in range( boxColumn*5,  boxColumn*5 + 5):
            for j in range(boxRow * 5, boxRow*5 + 5):
                if board[i][j] == num and [i,j]!=[row,col]:
                    return False
    

    else:
        print("Use your own mind to solve this, because i can't !")

    return True


def print_board(board):
    if(rows==4 and columns ==4):
        for i in range(len(board)):
            if i % 2 == 0 and i != 0:
                print("- - - - - - - - -  ")

            for j in range(len(board[0])):
                if j % 2 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    elif(rows==6 and columns ==6):
        for i in range(len(board)):
            if i % 2 == 0 and i != 0:
                print("- - - - - - - - - -  ")

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    elif(rows==8 and columns ==8):
        for i in range(len(board)):
            if i % 2 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(board[0])):
                if j % 4 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    elif(rows==9 and columns ==9):
        for i in range(rows):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(rows):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    elif(rows==10 and columns ==10):
        for i in range(len(board)):
            if i % 2 == 0 and i != 0:
                print("- - - - - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 5 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    elif(rows==12 and columns ==12):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 4 == 0 and j != 0:
                    print("   | ", end="   ")

                if j == columns-1:
                    print(board[i][j]+"   ")
                else:
                    print(str(board[i][j]) + "    ", end="  ")

    elif(rows==15 and columns ==15):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 5 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    elif(rows==16 and columns ==16):
        for i in range(len(board)):
            if i % 4 == 0 and i != 0:
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 4 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    elif(rows==25 and columns ==25):
        for i in range(len(board)):
            if i % 5 == 0 and i != 0:
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 5 == 0 and j != 0:
                    print(" | ", end="")

                if j == columns-1:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    else:
        print("Use your own mind to solve this, because i can't !")



def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i,j]  # row, col

    return None

print("\n\nEntered Sudoku Board :-\n")
print_board(sudoku_board)
sudokusolver(sudoku_board)
print("\n\nSolved :-----------------\n\n")
print_board(sudoku_board)  