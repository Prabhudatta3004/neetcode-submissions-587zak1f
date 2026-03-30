class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        def dfs(row,col):
            if (row<0 or col<0 or row>=ROWS or col>=COLS or
                grid[row][col] == "0"):
                return
            
            grid[row][col] = "0"

            for dr,dc in directions:
                nr,nc = row+dr, col+dc
                dfs(nr,nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count +=1
                    dfs(r,c)
        return count