# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# edge case: LL can be empty, or have one element 
## 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## head can be None
        if not head:
            return head
        ## if the linkedlist has only one node
        if not head.next:
            return head
        
        prev = None
        curr = head

        while curr:
          nxt = curr.next
          curr.next = prev
          prev = curr
          curr = nxt
        return prev  