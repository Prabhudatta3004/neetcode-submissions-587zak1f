# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while ptr1 or ptr2 or carry:
            if ptr1:
                val1 = ptr1.val
                ptr1 = ptr1.next
            else:
                val1 = 0
            if ptr2:
                val2 = ptr2.val
                ptr2 = ptr2.next
            else:
                val2 = 0

            total = (val1+val2+carry)
            new_node = ListNode(total%10)
            carry = total//10
            curr.next = new_node
            curr = curr.next
        return dummy.next