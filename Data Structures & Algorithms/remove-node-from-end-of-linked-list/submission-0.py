class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First pass: Count the number of nodes
        curr = head
        total = 0
        while curr:
            total += 1
            curr = curr.next
        
        # If we need to remove the head node
        if total == n:
            return head.next
        
        # Second pass: Stop at the node just before the target node
        curr = head
        for _ in range(total - n - 1):
            curr = curr.next
        # Remove the nth node from end
        curr.next = curr.next.next
        return head
