class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_time = 0
        fresh = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    queue.append((r,c,0))
        directions= [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            row,col,time = queue.popleft()
            max_time = max(max_time,time)
            for dr,dc in directions:
                new_row,new_col = dr+row, dc+col

                if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1):
                    grid[new_row][new_col] = 2
                    fresh -=1
                    queue.append((new_row,new_col,time+1))
        
        return max_time if fresh==0 else -1