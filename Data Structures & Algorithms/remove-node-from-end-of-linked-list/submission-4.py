class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node to simplify edge cases (like removing the head)
        dummy = ListNode(0, head)
        left = dummy
        right = dummy

        # Move right pointer n+1 steps ahead so left ends at node before target
        for _ in range(n + 1):
            right = right.next

        # Move both pointers until right hits the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node
        left.next = left.next.next

        return dummy.next
