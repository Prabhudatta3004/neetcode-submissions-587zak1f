# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1) ## this is my dummy node that will point to the new head
        temp = dummy ## my temp will always help in creating the sorted list
        t1 = list1
        t2 = list2

        ## I will change links till both the lists are non empty

        while t1 and t2:
            if t1.val <= t2.val:
                temp.next = t1
                t1= t1.next
                temp = temp.next
            elif t2.val < t1.val:
                temp.next = t2
                t2 = t2.next
                temp = temp.next
        
        ## If any of the list still exists we can straight away attach them

        if t1 : 
            temp.next = t1
        elif t2:
            temp.next = t2
        return dummy.next

