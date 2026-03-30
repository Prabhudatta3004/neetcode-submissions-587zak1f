# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ## either is empty I will return the non empty
        ## if both are empty I can return None
        ## list 1 I can pass 

        ## 1->2->3 1->3->5 
        ## 1->1->2->3->3->5
        ## dummy node , curr 

        dummy = ListNode(-1)
        curr = dummy
        temp_1 = list1
        temp_2 = list2

        while temp_1 and temp_2:
            ## compare the values
            if(temp_1.val <= temp_2.val):
                curr.next = temp_1
                temp_1 = temp_1.next
            else:
                curr.next = temp_2
                temp_2 = temp_2.next
            curr = curr.next
        if temp_1:
            curr.next = temp_1
        if temp_2:
            curr.next = temp_2
            
        return dummy.next


