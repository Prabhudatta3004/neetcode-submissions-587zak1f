class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        healthy = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==2:
                    queue.append((row,col,0))
                elif grid[row][col]==1:
                    healthy +=1
        max_time = 0
        while queue:
            row,col,time = queue.popleft()
            max_time = time
            for dr,dc in direction:
                new_row,new_col = row+dr,col+dc

                if(0<=new_row<ROWS and 0<=new_col<COLS and grid[new_row][new_col]==1):
                    grid[new_row][new_col] = 2
                    healthy -=1
                    queue.append((new_row,new_col,time+1))
        return max_time if healthy == 0 else -1

