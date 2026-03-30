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
        dummy = ListNode()
        temp = dummy

        while ptr1 or ptr2 or carry:

            if ptr1:
                value1 = ptr1.val
                ptr1 = ptr1.next
            else:
                value1 = 0
            
            if ptr2:
                value2 = ptr2.val
                ptr2 = ptr2.next
            else:
                value2 = 0
            
            sum_value = value1 + value2 + carry

            temp.next = ListNode(sum_value%10)
            carry = sum_value//10
            temp = temp.next
        return dummy.next
            
            