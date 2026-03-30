# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find middle (slow will stop at mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split and reverse second half
        head2 = slow.next
        slow.next = None  # cut the list into two halves

        prev, curr = None, head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev  # now head2 is the reversed half

        # Step 3: Merge two halves
        head1 = head
        while head1 and head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2
