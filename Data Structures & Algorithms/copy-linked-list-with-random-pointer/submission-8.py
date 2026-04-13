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
        curr = head

        while curr:
            nxt = curr.next
            new_node = Node(curr.val)
            curr.next = new_node
            new_node.next = nxt

            curr = curr.next.next
        
        ## to copy the random pointers
        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        ## now removing new node
        dummy = Node(0)
        temp = dummy
        curr = head

        while curr:
            temp.next = curr.next
            temp = temp.next

            curr.next = curr.next.next
            curr = curr.next
        return dummy.next
            