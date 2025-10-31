
def solveSudoku(board):
    def isSafe(board,row,col,dig):
        for i in range(9):
            if board[i][col]==str(dig):
                return False
        
        for j in range(9):
            if board[row][j]==str(dig):
                return False
        
        sr=(row//3)*3
        sc=(col//3)*3
        for i in range(sr,sr+3):
            for j in range(sc,sc+3):
                if board[i][j]==str(dig):
                    return False
        return True


    def sudoko(board, row=0, col=0):
        if row == 9:
            return True  # Solved

        if col == 9:
            return sudoko(board, row + 1, 0)

        if board[row][col] != ".":
            return sudoko(board, row, col + 1)

        for dig in range(1, 10):
            if isSafe(board, row, col, dig):
                board[row][col] = str(dig)
                if sudoko(board, row, col + 1):
                    return True
                board[row][col] = "."  # Backtrack

        return False
    sudoko(board,0,0)
    return board
