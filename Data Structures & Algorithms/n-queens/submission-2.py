class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Sets to track which columns and diagonals are currently under attack
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)
        
        res = []
        # Create an empty N x N board
        board = [["."] * n for _ in range(n)]
        
        def backtrack(row):
            # Base Case: If we've successfully placed a queen in every row
            if row == n:
                # Format the board into a list of strings as LeetCode expects
                formatted_board = ["".join(r) for r in board]
                res.append(formatted_board)
                return
            
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if the current square is attacked
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue  # Skip this column, it's not safe
                
                # 1. DO: Place the queen and mark her attack lines
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = "Q"
                
                # 2. RECURSE: Move to the next row
                backtrack(row + 1)
                
                # 3. UNDO: Remove the queen and her attack lines
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = "."
                
        # Start the backtracking process at row 0
        backtrack(0)
        return res