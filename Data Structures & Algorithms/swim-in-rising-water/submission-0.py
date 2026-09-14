class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N= len(grid)

        direction = [(1,0),(0,1),(-1,0),(0,-1)]

        minheap = [(grid[0][0],0,0)]
        visited = set()
        while minheap:
            curr_max,r,c = heapq.heappop(minheap)

            if r==N-1 and c==N-1:
                return curr_max
            
            for dr,dc in direction:
                new_row,new_col= r+dr,c+dc
                if (0<=new_row<N and 0<=new_col<N and (new_row,new_col) not in visited):
                    visited.add((new_row,new_col))
                    new_max = max(curr_max,grid[new_row][new_col])
                    heapq.heappush(minheap,(new_max,new_row,new_col))
