import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        heap = []
        
        # Step 1: Push all the heads into the heap
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        
        dummy = ListNode(-1)
        curr = dummy
        
        # Step 2: Pop smallest, attach, push next if exists
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
