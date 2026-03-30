class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def backtrack(r,c,i):
            if i == len(word):
                return True
            
            if r<0 or r>=ROWS or c<0 or c>=COLS or word[i] != board[r][c] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if backtrack(nr,nc,i+1):
                    return True
            visited.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        return False