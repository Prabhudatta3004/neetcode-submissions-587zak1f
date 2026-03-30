
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequencies
        count = defaultdict(int)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        minheap = []
        
        # Step 2: Iterate over the UNIQUE keys in the map
        # FIXED: Use count.items() instead of nums
        for num, freq in count.items():
            heapq.heappush(minheap, (freq, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        # Step 3: Extract results safely
        # FIXED: List comprehension extracts without unsafe popping
        return [num for freq, num in minheap]