class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row,col):
            grid[row][col] = "0"
            for dr,dc in directions:
                new_row,new_col = row+dr,col+dc
                if(0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]=="1"):
                    grid[new_row][new_col] = "0"
                    dfs(new_row,new_col)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands +=1
                    dfs(row,col)
        return islands