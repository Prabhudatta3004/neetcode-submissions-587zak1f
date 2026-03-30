# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## finding mid

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middle = slow

        ## separate two ll

        new_head = middle.next
        middle.next = None

        def reverse(head):
            temp = head
            prev = None
            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            return prev

        new_head = reverse(new_head)

        temp1 = head
        temp2 = new_head
        while temp1 and temp2:
            nxt1 = temp1.next
            nxt2 = temp2.next
            
            temp1.next = temp2
            temp2.next = nxt1
            
            temp1 = nxt1
            temp2 = nxt2
