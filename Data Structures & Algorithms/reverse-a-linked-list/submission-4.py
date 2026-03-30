# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two checks: No LL, and another is only one node : Head
        # 1->2 : 2->1
        # 1->2->3 : stack will store the node.val 
        # 1-> 2 : 2->1 
        # prev, nxt , curr.next = nxt, curr.next = prev
        ## prev = curr, curr = next 
        ## 1->2->3 
        
        if not head:
            return head
        if not head.next:
            return head
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        ## test-case:01 : 1
        ## test-case:02 : 1->2->3
        ## test-case: 03 : None
        

