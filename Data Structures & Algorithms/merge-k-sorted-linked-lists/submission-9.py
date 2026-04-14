import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        # Use a unique counter to prevent comparing ListNode objects
        count = 0 
        
        for l in lists:
            if l:
                heapq.heappush(minheap, (l.val, count, l))
                count += 1
        
        dummy = ListNode()
        curr = dummy
        
        while minheap:
            val, _, node = heapq.heappop(minheap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                count += 1
                heapq.heappush(minheap, (node.next.val, count, node.next))
        
        return dummy.next