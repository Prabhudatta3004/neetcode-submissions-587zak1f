# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] ## minheap
        counter = 0 ## to break ties
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter,node))
            counter +=1
        dummy = ListNode(-1)
        temp = dummy

        while heap:
            val, _ , node = heapq.heappop(heap)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter +=1

        return dummy.next
