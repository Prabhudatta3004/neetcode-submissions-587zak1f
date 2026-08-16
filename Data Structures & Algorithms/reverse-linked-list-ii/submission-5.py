# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            curr = head
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        dummy = ListNode()
        dummy.next = head

        left_ptr = right_ptr = dummy

        for _ in range(right):
            right_ptr = right_ptr.next
        
        next_to_right = right_ptr.next
        right_ptr.next = None
        
        for _ in range(left-1):
            left_ptr = left_ptr.next
        
        new_head = left_ptr.next
        
        left_ptr.next = reverse(new_head)

        new_head.next = next_to_right

        return dummy.next
            