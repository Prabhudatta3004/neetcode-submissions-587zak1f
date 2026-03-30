# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(minheap, (node.val,counter, node))
                counter +=1
        
        dummy = ListNode()
        temp = dummy
        while minheap:
            _,counter,node = heapq.heappop(minheap)

            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(minheap, (node.next.val, counter, node.next))
                counter +=1
        return dummy.next