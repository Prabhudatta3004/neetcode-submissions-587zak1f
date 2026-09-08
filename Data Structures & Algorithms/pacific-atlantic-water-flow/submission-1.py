class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]

        pacific_queue = deque()
        atlantic_queue = deque()
        pacific_set = set()
        atlantic_set = set()

        ## lets put all the queues
        ## lets first fill the rows
        for c in range(cols):
            pacific_queue.append((0,c))
            pacific_set.add((0,c))

            atlantic_queue.append((rows-1,c))
            atlantic_set.add((rows-1,c))
        ## lets fill the cols
        for r in range(rows):
            pacific_queue.append((r,0))
            pacific_set.add((r,0))

            atlantic_queue.append((r,cols-1))
            atlantic_set.add((r,cols-1))

        def bfs(queue,present_set):

            while queue:
                r,c = queue.popleft()
                for dr,dc in direction:
                    new_row, new_col = dr+r,dc+c
                    if(0<=new_row<rows and 0<=new_col<cols and (new_row,new_col) not in present_set and heights[new_row][new_col]>= heights[r][c]):
                        present_set.add((new_row,new_col))
                        queue.append((new_row,new_col))
        
        bfs(pacific_queue,pacific_set)
        bfs(atlantic_queue,atlantic_set)
        res =[]
        for r in range(rows):
            for c in range(cols):
                if ((r,c) in pacific_set and (r,c) in atlantic_set):
                    res.append([r,c])
        return res

