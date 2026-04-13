# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        
        dummy = ListNode()
        temp = dummy
        carry = 0

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
            total_val = val1 + val2 + carry
            
            new_node = ListNode(total_val%10)
            carry = total_val // 10

            temp.next = new_node
            temp = temp.next
        return dummy.next