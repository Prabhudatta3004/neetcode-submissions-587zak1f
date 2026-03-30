class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows-1 or col == 0 or
                    col == cols-1):
                    if board[row][col] == "O":
                        board[row][col] = "T"
                        queue.append((row,col))

        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr,nc= r+dr,c+dc
                if (0<=nr<rows and 0<=nc<cols and board[nr][nc] == "O"):
                    board[nr][nc] = "T"
                    queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
            
