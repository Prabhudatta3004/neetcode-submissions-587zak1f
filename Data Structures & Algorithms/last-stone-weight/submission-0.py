import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert the list into a max heap using negative values
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)  # O(n)

        # Keep smashing the two heaviest stones
        while len(maxHeap) > 1:
            # Get the two heaviest stones (note the negative values)
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            if first != second:
                # Push the difference back into the heap as negative
                heapq.heappush(maxHeap, -(first - second))

        # If one stone is left, return it (negated), else return 0
        return -maxHeap[0] if maxHeap else 0
