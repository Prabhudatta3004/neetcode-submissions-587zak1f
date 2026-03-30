class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        carry = 0
        dummy = ListNode()
        temp = dummy
        while temp1 or temp2 or carry:
            if temp1:
                num1 = temp1.val
                temp1 = temp1.next
            else:
                num1 = 0
            
            if temp2:
                num2 = temp2.val
                temp2 = temp2.next
            else:
                num2 = 0
            
            sum_val = num1 + num2 + carry
            val = sum_val % 10
            carry = sum_val // 10

            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next