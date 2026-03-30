# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)

        p1 = list1
        p2 = list2
        curr = dummy_node
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            elif p2.val <  p1.val:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        
        if p1:
            curr.next =p1
            curr = curr.next
        if p2:
            curr.next =p2
            curr = curr.next

        return dummy_node.next
        
