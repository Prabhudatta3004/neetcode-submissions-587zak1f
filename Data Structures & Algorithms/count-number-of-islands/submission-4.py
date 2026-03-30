class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        islands = 0

        def dfs(row,col):
            grid[row][col] = "0"

            for dr, dc in directions:
                nr,nc = row+dr,col+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1":
                    dfs(nr,nc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands +=1
                    dfs(row,col)
        return islands