# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list:
            return []
        minheap = []

        for idx,node in enumerate(lists):
            if node:
                heapq.heappush(minheap,(node.val,idx,node))
        
        dummy = ListNode()
        curr =dummy
        while minheap:
            val,idx,node = heapq.heappop(minheap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minheap,(node.next.val,idx,node.next))
        return dummy.next