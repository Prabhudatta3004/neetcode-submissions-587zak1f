class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        def bfs(row,col):
            area = 1
            queue = deque()
            grid[row][col] = 0
            queue.append((row,col))

            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 0
                        area +=1
                        queue.append((nr,nc))
            return area
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = bfs(row,col)
                    max_area = max(max_area,area)
        return max_area