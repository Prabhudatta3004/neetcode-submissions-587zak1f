# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # No LL
        # 1>2>3>4>None-- fast != None
        # 1>2>3>None : fast.next != None

        if not head:
            return False
        
        fast, slow = head,head

        ## Lets check for loop
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False