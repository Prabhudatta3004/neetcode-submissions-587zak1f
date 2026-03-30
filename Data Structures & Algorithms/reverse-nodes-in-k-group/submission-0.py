# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ## helper to find kth node starting from node
        def find_kth(node, k):
            while node and k > 1:
                node = node.next
                k -= 1
            return node
        
        ## helper to reverse a linked list segment
        def reverse_segment(start, end):
            prev = None
            curr = start
            stop = end.next
            while curr != stop:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, start  # new head, new tail
        
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            kth = find_kth(group_prev.next, k)
            if not kth:  # fewer than k nodes remain
                break
            group_next = kth.next
            
            # reverse current k-group
            new_head, new_tail = reverse_segment(group_prev.next, kth)
            
            # connect reversed group back
            group_prev.next = new_head
            new_tail.next = group_next
            
            # move to next group
            group_prev = new_tail
        
        return dummy.next
