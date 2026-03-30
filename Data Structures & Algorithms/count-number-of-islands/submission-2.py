class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        row_boundary = len(grid)
        col_boundary = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        def bfs(row,col):
            queue= deque()
            queue.append((row,col))
            grid[r][c] = "0"

            while queue:
                row,col = queue.popleft()
                for dr,dc in directions:
                    new_row,new_col = row+dr,col+dc
                    if(0<=new_row<row_boundary and 0<=new_col<col_boundary
                        and grid[new_row][new_col]=="1"):

                        grid[new_row][new_col] = "0"
                        queue.append((new_row,new_col))

        for r in range(row_boundary):
            for c in range(col_boundary):
                if grid[r][c] == "1":
                    counter+=1
                    bfs(r,c)
        return counter 