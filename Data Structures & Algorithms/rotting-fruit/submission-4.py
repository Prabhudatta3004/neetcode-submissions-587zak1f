class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions= [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        fresh= 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh +=1
                elif grid[row][col] == 2:
                    queue.append((row,col,0))
        max_time = 0
        while queue:
            r,c, time = queue.popleft()
            max_time = max(max_time, time)

            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1):
                    grid[nr][nc] = 2
                    fresh -=1
                    queue.append((nr,nc,time+1))
        return max_time if fresh ==0 else -1