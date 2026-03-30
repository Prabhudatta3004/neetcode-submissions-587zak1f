import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # --- CHUNK 1: Preprocessing ---
        new_task = []
        for i, t in enumerate(tasks):
            # arrival time, proc_time, index
            new_task.append([t[0], t[1], i]) 
        
        new_task.sort() 

        # --- CHUNK 2: Setup ---
        time = 0
        minheap = []
        res = []
        i = 0
        
        # --- CHUNK 3: Simulation ---
        while minheap or i < len(new_task):
            
            if not minheap and time < new_task[i][0]:
                time = new_task[i][0]

            # Fill the Waiting Room
            while i < len(new_task) and new_task[i][0] <= time:
                heapq.heappush(minheap, (new_task[i][1], new_task[i][2]))
                i += 1
            
            # Do the Work
            if minheap:
                proc_time, index = heapq.heappop(minheap)
                time += proc_time
                res.append(index)
                
        return res