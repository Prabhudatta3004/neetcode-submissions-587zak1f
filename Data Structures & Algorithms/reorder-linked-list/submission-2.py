# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## Step : 01 find the middle of the LL
        ## Step : 02 remove from middle till end
        ## Step: 03 Reverse the second half of the list
        ## Step: 04 Create a new list with the first half and second half

        ## step:01

        slow,fast = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        ## slow has the last element of the first half

        second_head = slow.next
        slow.next = None

        ## Step:03

        prev = None
        curr = second_head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        ## prev is head of the reversed second half

        head_2 = prev
        head_1 = head

        temp_1 = head_1
        temp_2 = head_2
        
        while temp_1 and temp_2:
            next_1 = temp_1.next
            next_2 = temp_2.next

            temp_1.next = temp_2

            if not temp_1:
                break
            
            temp_2.next = next_1

            temp_1 = next_1
            temp_2 = next_2
            