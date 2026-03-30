from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)

        # Step 2: Create a max heap using negative counts
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        # Step 3: Cooldown queue to hold tasks that are cooling down
        # Each entry is a tuple: (time_when_ready, count)
        cooldown = deque()

        # Step 4: Time tracker
        time = 0

        # Step 5: Simulate each CPU time unit
        while max_heap or cooldown:
            time += 1  # Advance time

            # Step 5.1: Check if any task's cooldown is done
            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(max_heap, count)

            # Step 5.2: Run the task with the highest remaining frequency
            if max_heap:
                count = heapq.heappop(max_heap)
                if count + 1 != 0:  # More of this task remains
                    # Add it to cooldown with updated count and ready time
                    cooldown.append((time + n + 1, count + 1))
            # else: No task to run this cycle (CPU is idle)

        return time
