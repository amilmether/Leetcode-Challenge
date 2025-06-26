# 36. Valid Sudoku [Medium]
# Tags: misc
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squar = defaultdict(set)
        for r in range(9):
            for c in range(9):
                
                if board[r][c] != ".":
                    if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squar[(r//3,c//3)]):
                        return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squar[(r//3,c//3)].add(board[r][c])        
        return True