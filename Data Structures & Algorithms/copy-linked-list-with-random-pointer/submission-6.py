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
        temp = head
        while temp:
            new_node = Node(temp.val)
            #new_node.val = temp.val
            nxt = temp.next
            temp.next = new_node
            new_node.next = nxt
            temp = temp.next.next
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        dummy = Node(0)
        curr = dummy

        temp  = head

        while temp:
            curr.next = temp.next
            temp.next = temp.next.next
            curr = curr.next
            temp = temp.next
        return dummy.next