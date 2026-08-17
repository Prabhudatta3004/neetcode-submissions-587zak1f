# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []

        for i,node in enumerate(lists):
            heapq.heappush(minheap,(node.val,i,node))
        
        dummy = ListNode()
        curr = dummy

        while minheap:
            val,i,node = heapq.heappop(minheap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minheap,(node.next.val,i,node.next))
        return dummy.next