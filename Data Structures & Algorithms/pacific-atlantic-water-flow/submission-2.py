class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        pacific_queue = deque()
        atlantic_queue = deque()
        pacific_set = set()
        atlantic_set = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ## filling the rows,0th row with pacific,row-1 with atlantic
        for c in range(COLS):
            pacific_queue.append((0,c))
            atlantic_queue.append((ROWS-1,c))
            pacific_set.add((0,c))
            atlantic_set.add((ROWS-1,c))
        
        for r in range(ROWS):
            pacific_queue.append((r,0))
            pacific_set.add((r,0))
            atlantic_queue.append((r,COLS-1))
            atlantic_set.add((r,COLS-1))
        
        def bfs(queue,current_set):

            while queue:
                row,col = queue.popleft()
                for dr,dc in directions:
                    new_row,new_col = row+dr,col+dc

                    if(0<=new_row<ROWS and 0<=new_col<COLS and (new_row,new_col) not in current_set and grid[new_row][new_col]>=grid[row][col]):
                        current_set.add((new_row,new_col))
                        queue.append((new_row,new_col))
        
        bfs(pacific_queue,pacific_set)
        bfs(atlantic_queue,atlantic_set)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_set and (r,c) in atlantic_set:
                    res.append([r,c])
        return res
