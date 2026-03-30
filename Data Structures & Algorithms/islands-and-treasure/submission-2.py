class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        INF = 2147483647
        queue = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if (0<=nr<ROWS and 0<=nc<COLS 
                    and grid[nr][nc] == INF):

                    if((nr,nc) not in visited):
                        grid[nr][nc] = grid[r][c] + 1
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        # return grid



