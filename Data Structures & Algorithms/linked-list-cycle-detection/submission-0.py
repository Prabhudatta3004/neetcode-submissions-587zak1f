# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lookup_set = []

        curr = head

        while curr:
            if curr.next in lookup_set:
                return True
            else:
                lookup_set.append(curr.next)
            curr = curr.next
        return False