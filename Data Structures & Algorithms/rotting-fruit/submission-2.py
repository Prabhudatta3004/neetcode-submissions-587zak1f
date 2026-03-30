class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                if grid[r][c] == 1:
                    fresh +=1
        time = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            r,c,t = queue.popleft()
            time = max(time, t)
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if (0<=nr<ROWS and 0<=nc<COLS and 
                    grid[nr][nc] == 1):
                    grid[nr][nc] =2 
                    fresh -=1
                    queue.append((nr,nc,t+1))
        return time if fresh == 0 else -1