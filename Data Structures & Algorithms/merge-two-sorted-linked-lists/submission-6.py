# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode()
        temp3 = dummy

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp3.next = temp1
                temp3 = temp3.next
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp3 = temp3.next
                temp2 = temp2.next
        
        if temp1:
            temp3.next = temp1
        if temp2:
            temp3.next = temp2

        return dummy.next