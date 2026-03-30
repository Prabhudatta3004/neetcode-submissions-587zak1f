class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        max_area = 0

        def bfs(row,col):
            component_area = 1
            queue = deque()
            grid[row][col] = 0
            queue.append((row,col))

            while queue:
                r,c = queue.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr,dc in directions:
                    new_row,new_col = r+dr, c+dc
                    if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 0
                        component_area +=1
                        queue.append((new_row,new_col))
            return component_area

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = bfs(row,col)
                    max_area = max(max_area,area)
        
        return max_area