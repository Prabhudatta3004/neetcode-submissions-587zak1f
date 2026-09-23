class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==0:
                    queue.append((row,col,0))
        
        while queue:
            row,col,prev_val = queue.popleft()

            for dr,dc in directions:
                new_row,new_col = dr+row,dc+col

                if(0<=new_row<ROWS and 0<=new_col<COLS and grid[new_row][new_col]==INF):
                    grid[new_row][new_col] = 1+prev_val
                    queue.append((new_row,new_col,grid[new_row][new_col]))
        
