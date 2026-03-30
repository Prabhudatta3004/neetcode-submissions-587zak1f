class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0)) ## passing all the rotten oranges at t=0
                elif grid[i][j] == 1:
                    fresh +=1
        
        time = 0
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        while queue:
            r,c , t = queue.popleft()
            time = max(time,t)
            for dr,dc in directions:
                new_row,new_col = r+dr,c+dc

                ## conditions
                if (0<=new_row<m and 0<=new_col<n and
                    grid[new_row][new_col] == 1):
                    grid[new_row][new_col] = 2
                    fresh -=1
                    queue.append((new_row,new_col,t+1))

        return time if fresh == 0 else -1



        
