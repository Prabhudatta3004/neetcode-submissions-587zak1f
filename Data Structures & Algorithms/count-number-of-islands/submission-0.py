class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        m = len(grid)
        n = len(grid[0])

        num_islands = 0

        def bfs(row,col):
            queue = deque()
            grid[row][col] = "0"
            queue.append((row,col))

            while queue:
                r,c = queue.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    new_row,new_col = r+dr,c+dc
                    if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col] == "1":
                        grid[new_row][new_col] = "0"
                        queue.append((new_row,new_col))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    num_islands += 1
                    bfs(row,col)

        return num_islands