class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh +=1

        time = 0
        while queue:
            row,col,node_time = queue.popleft()
            time = max(time, node_time)
            Directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in Directions:
                new_row,new_col = row+dr, col+dc
                if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh -=1
                    queue.append((new_row,new_col,time+1))

        
        return -1 if fresh>0 else time