def isValidSudoku(board):
        rows=[[] for i in range(9)] # rows[i] is a list of  all the digits in the ith rows
        columns=[[] for i in range(9)]  # rows[i] is a list of  all the digits in the ith columns
        cells={}  # cells[(i,j)] is a list of  all the digits in the 3*3 grid from 3*i to 3*i+2 and 3*j to 3*j+2
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c]:
                    return False
                if board[r][c] in cells.get((r//3,c//3),[]):
                    return False
                rows[r].append(board[r][c])
                columns[c].append(board[r][c])
                cells[(r//3,c//3)]=cells.get((r//3,c//3),[])+[board[r][c]]
        
        return True
# complexity of O(1)  

        
