# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy

        p1 = l1
        p2 = l2
        carry = 0

        while p1 or p2 or carry>0:

            if p1:
                val1 = p1.val
                p1 = p1.next
            else:
                val1= 0

            if p2:
                val2 = p2.val
                p2 = p2.next
            else:
                val2 = 0
            
            total = val1 + val2 + carry
            new_node = ListNode(total%10)
            carry = total//10
            curr.next = new_node
            curr = curr.next
        return dummy.next

