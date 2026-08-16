"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ## creating the copies
        if not head:
            return None
        
        curr = head
        while curr:
            new_node = Node(curr.val)
            nxt = curr.next
            curr.next = new_node
            new_node.next = nxt
            curr = nxt
        
        ## adjusting the random pointers
        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        ## now we need to separate these two threads

        dummy = Node(0)
        #dummy.next = head.next
        curr = dummy
        #curr = curr.next

        curr1 = head

        while curr1:
            curr.next = curr1.next
            curr = curr.next
            curr1.next = curr1.next.next
            curr1 = curr1.next
        return dummy.next

