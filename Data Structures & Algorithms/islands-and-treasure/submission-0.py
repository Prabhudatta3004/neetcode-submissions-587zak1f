class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        m = len(grid)
        n = len(grid[0])
        Directions = [(1,0),(-1,0),(0,-1),(0,1)]

        queue = deque()
        
        for rows in range(m):
            for cols in range(n):
                if grid[rows][cols] == 0:
                    queue.append((rows,cols))

        while queue:
            curr_row,curr_col = queue.popleft()
            for dr,dc in Directions:
                new_row,new_col = curr_row+ dr , curr_col + dc
                if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col] == INF:
                    grid[new_row][new_col] = grid[curr_row][curr_col] + 1
                    queue.append((new_row,new_col))

            
