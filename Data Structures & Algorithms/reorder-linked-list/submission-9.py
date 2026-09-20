# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head):
            curr = head
            nxt,prev = None,None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        new_head = slow.next
        mid.next = None

        new_head = reverse(new_head)

        ptr1 = head
        ptr2 = new_head

        while ptr2:
            tmp1,tmp2 = ptr1.next,ptr2.next
            ptr1.next = ptr2
            ptr2.next = tmp1
            ptr1 = tmp1
            ptr2 = tmp2
            