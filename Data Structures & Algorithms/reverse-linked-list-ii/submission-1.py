class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # Dummy node for safety when reversing from index 1
        dummy = ListNode(0, head)
        
        # 1. Move `before_left` to the node before the `left` position
        before_left = dummy
        for _ in range(left - 1):
            before_left = before_left.next
        
        # 2. Move `right_node` to the `right` position
        right_node = dummy
        for _ in range(right):
            right_node = right_node.next
        
        # 3. Store the next section
        after_right = right_node.next
        
        # 4. Detach sublist
        right_node.next = None
        
        # 5. Reverse sublist
        new_head = reverse(before_left.next)
        
        # 6. Reconnect
        before_left.next.next = after_right
        before_left.next = new_head
        
        return dummy.next
