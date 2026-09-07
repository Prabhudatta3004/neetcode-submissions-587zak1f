class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))
            
        while queue:
            r,c= queue.popleft()
            for dr,dc in directions:
                new_row,new_col = r+dr,c+dc
                if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]== INF):
                    grid[new_row][new_col] = grid[r][c] + 1
                    queue.append((new_row,new_col))
            
        