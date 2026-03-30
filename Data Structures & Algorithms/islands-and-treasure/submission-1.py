class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row,col))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                new_row,new_col = r+dr,c+dc

                if (0<=new_row<m and 0<=new_col<n and grid[new_row][new_col]==INF):
                    grid[new_row][new_col] = grid[r][c]+1
                    queue.append((new_row,new_col))
            