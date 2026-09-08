class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if(r==0 or r==rows-1 or c==0 or c==cols-1):
                    if board[r][c] == "O":
                        board[r][c] = "T"
                        queue.append((r,c))
        
        while queue:
            r,c = queue.popleft()
            for dr,dc in direction:
                nr,nc = r+dr,c+dc
                if(0<=nr<rows and 0<=nc<cols and board[nr][nc]=="O"):
                    board[nr][nc] = "T"
                    queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
    