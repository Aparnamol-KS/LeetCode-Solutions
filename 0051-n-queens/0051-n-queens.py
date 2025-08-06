def canPlace(board, row, col):
    n = len(board)

    # same column
    i = row
    j = col
    while i >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1

    # diagonal 1
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1


    # diagonal 2
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True

def deepCopy(board):
    res = []

    for i in range(len(board)):
        cur_row = "".join(board[i])
        res.append(cur_row)
    
    return res

def nQueensSolver(board, row, ans):
    n = len(board)

    if row == n:
        ans.append(deepCopy(board))
        return ans

    for j in range(n):
        if canPlace(board, row, j):
            board[row][j] = 'Q'
            nQueensSolver(board, row + 1, ans) 
            board[row][j] = '.'

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        ans = []

        board = [] # n * n, all cells should be empty
        for i in range(n):
            row = []
            for j in range(n):
                row.append('.')
            board.append(row)

        nQueensSolver(board, 0, ans)

        return ans