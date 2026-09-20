# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        count = 0
        for head in lists:
            count +=1
            if head:
                heapq.heappush(minheap,(head.val,count,head))
        dummy = ListNode()
        curr = dummy
        while minheap:
            val,count,head = heapq.heappop(minheap)
            curr.next = head
            curr = curr.next
            if head.next:
                heapq.heappush(minheap,(head.next.val,count,head.next))
            count +=1
        return dummy.next
