class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647 ## for land
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        #dist = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]== INF):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
        