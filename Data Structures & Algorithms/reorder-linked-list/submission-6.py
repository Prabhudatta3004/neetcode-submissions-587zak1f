# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
            
        # STEP 1: Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # STEP 2: Reverse the second half
        curr = slow.next
        slow.next = None  # CRITICAL: Sever the first half from the second half
        
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # STEP 3: Merge the two halves (Weave them together)
        first = head
        second = prev   # 'prev' is the head of the reversed second half
        
        while second:
            # Save the original next nodes before we overwrite the pointers
            tmp1 = first.next
            tmp2 = second.next
            
            # Point the first node to the second node
            first.next = second
            
            # Point the second node to the next node in the first half
            second.next = tmp1
            
            # Move both pointers forward for the next iteration
            first = tmp1
            second = tmp2