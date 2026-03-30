# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp1 = l1
        temp2 = l2
        dummy = ListNode(-1)
        temp = dummy

        while temp1 or temp2 or carry:
            if temp1:
                value1 = temp1.val
            else:
                value1 = 0
            if temp2:
                value2 = temp2.val
            else:
                value2 = 0
            
            value = (value1+value2+carry)%10
            carry = (value1+value2+carry)//10
            temp.next = ListNode(value)

            temp = temp.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        return dummy.next
            