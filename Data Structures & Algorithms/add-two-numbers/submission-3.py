# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## 321 , LL 1>2>3 , 1024 , LL : 4>2>0>1
        ## 321+1024 
        ## carryover >9, 

        ## 123+981 = 0 sum % 10, sum//10 == carry
        ## carry = //10, %10

        ##value = (value1 + value2 + carry) % 10
        ## carry = (value1 + value2 + carry) //10
        
        ## 100 + 901 = 1001

        ## value1  = val , 0
        ## value2 ...
        ## carry = 0

        ## two pointer and carry

        temp1 = l1
        temp2 = l2
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while temp1 or temp2 or carry:
            if temp1:
                value1 = temp1.val
            else:
                value1 = 0
            
            if temp2:
                value2 = temp2.val
            else:
                value2 = 0
            
            value = (value1+value2+carry) % 10
            carry = (value1+value2+carry) // 10
            curr.next = ListNode(value)

            curr = curr.next

            if temp1:
                temp1 = temp1.next
            
            if temp2:
                temp2 = temp2.next
        return dummy.next

