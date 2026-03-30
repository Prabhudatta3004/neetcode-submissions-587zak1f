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
        ## Creation and insertion of the Copy_Nodes
        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next.next
        
        ## Updating the random pointers 
        temp = head
        while temp:
            if temp.random:
                temp.next.random =temp.random.next
            temp = temp.next.next

        ## Now we need to detach the copied LL
        ## while preserving the original LL
        dummy = Node(-1)
        res = dummy
        temp = head
        while temp:
            res.next = temp.next
            temp.next = temp.next.next
            temp = temp.next
            res = res.next
        return dummy.next