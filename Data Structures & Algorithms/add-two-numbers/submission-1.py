# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode(-1)
        temp = dummy_node
        carry = 0
        temp1= l1
        temp2 = l2
        while temp1 or temp2 or carry:
            
            if temp1 : 
                val1 = temp1.val 
            else:
                val1 = 0
            if temp2 : 
                val2 = temp2.val
            else:
                val2 = 0
            
            val = (val1+val2+carry) % 10
            carry = (val1+val2+carry) // 10
            temp.next = ListNode(val)

            if temp1:
                temp1 = temp1.next
            else:
                temp1 = None
            if temp2:
                temp2 = temp2.next
            else:
                temp2 = None
            temp = temp.next
        return dummy_node.next
