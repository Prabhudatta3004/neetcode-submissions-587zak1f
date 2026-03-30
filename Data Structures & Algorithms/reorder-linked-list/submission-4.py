# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        ## find the middle element
        ## break the linked list
        ## reverse the second half
        ## reattach the LL

        ## finding the middle element

        slow,fast = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middle = slow

        second_head = middle.next

        middle.next = None

        prev = None

        temp = second_head

        while temp:
            nxt=temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        second_head = prev

        ## we have two lists
        temp1 = head
        temp2 = second_head
        
        while temp2:
            next1 = temp1.next
            next2 = temp2.next
            temp1.next = temp2
            temp2.next = next1
            temp1 = next1
            temp2 = next2
        