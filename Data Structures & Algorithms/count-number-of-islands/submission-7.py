class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Directions = [(1,0),(-1,0),(0,-1),(0,1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row,col):
            grid[row][col] ="0"
            for dr,dc in Directions:
                new_row,new_col = row+dr,col+dc
                if(0<=new_row<ROWS and 0<=new_col<COLS and 
                grid[new_row][new_col]=="1"):
                    dfs(new_row,new_col)

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    count +=1
                    dfs(row,col)
        return count