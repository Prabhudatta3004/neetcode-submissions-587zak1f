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
        ## to copy we need 3 things, one is val
        ## the other is the next pointer
        ## the third is the random pointet
        ## let me create the list first

        temp = head

        while temp:
            nxt = temp.next
            new_node = Node(temp.val)
            temp.next = new_node
            new_node.next = nxt
            temp = nxt

        
        ## now I need to assign the random pointers

        temp = head

        while temp and temp.next:
            if temp.random:
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp = temp.next.next


        ## detach the new list from old

        dummy = Node(-1)
        new_pointer = dummy
        old_pointer = head

        while old_pointer:
            new_pointer.next = old_pointer.next
            old_pointer.next = old_pointer.next.next
            new_pointer = new_pointer.next
            old_pointer = old_pointer.next
        
        return dummy.next