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
        left -=1
        dummy = ListNode(0,head)

        right_ptr = left_ptr = dummy

        while right:
            right_ptr = right_ptr.next
            right -=1
        
        node_after_right = right_ptr.next
        right_ptr.next = None 

        while left:
            left_ptr = left_ptr.next
            left -=1
        
        node_before_left = left_ptr
        new_head = left_ptr.next
        left_ptr.next = None

        node_before_left.next = reverse(new_head)

        new_head.next = node_after_right

        return dummy.next

