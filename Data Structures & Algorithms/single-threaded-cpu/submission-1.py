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
            
            # LOGIC FIX 1: Remove "time += 1". 
            # We only move time forward if we are jumping gaps or working.
            
            # LOGIC FIX 2: Handle Idle CPU
            # If we have no work (empty heap) but tasks are coming...
            if not minheap and i < len(new_task):
                # Jump straight to the arrival time. 
                # We use max() just in case 'time' is already ahead (unlikely if heap is empty, but safe).
                time = max(time, new_task[i][0])

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