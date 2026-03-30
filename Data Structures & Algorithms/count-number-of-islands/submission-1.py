class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        new_island = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(row,col):
            
            queue = deque()
            queue.append((row,col))
            grid[row][col] = "0"
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                r,c = queue.popleft()

                for dr,dc in directions:
                    new_row,new_col = r+dr,c+dc

                    ##checking boundaries
                    if(0<=new_row<m and 0<=new_col<n and grid[new_row][new_col]=="1"):
                        grid[new_row][new_col] = "0"

                        queue.append((new_row,new_col))


        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    new_island +=1
                    bfs(row,col)

        return new_island
        
        