# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minheap = []
        count = 0

        for node in lists:
            if node:
                heapq.heappush(minheap,(node.val,count,node))
                count +=1
            
        dummy = ListNode()
        temp = dummy

        while minheap:
            _,count,node = heapq.heappop(minheap)

            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(minheap,(node.next.val, count, node.next))
                count +=1
        
        return dummy.next