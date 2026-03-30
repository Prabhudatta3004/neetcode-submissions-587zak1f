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
        ## to create the new nodes first, along with the next
        ## 3>7>4>5
        ## 3>3>7>7>4>4>5>5
        
        ## deep copy of the normal LL
        ## create new nodes, curr nodes -> next preserved
        ## curr.next = new_node
        ## new_node.next = nxt
        temp = head

        while temp:
            nxt = temp.next
            new_node = Node(temp.val)
            temp.next = new_node
            new_node.next = nxt
            temp = nxt
        
        ## have another pass for the random pointer: future , Null
        ## 3>7>4>5 curr.random = 4, 
        ## 3>3>7>7>4>4>5 curr.next.random = curr.random.next

        ## curr.next.random = None

        curr = head

        while curr and curr.next :
            if curr.random :
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
        
        # dummy : connect with new_nodes
        # temp : original LL

        ## 3>3>4>4>5>5>6>6, dummy>new pointer, ol
        dummy = Node(-1)
        new_pointer = dummy
        old_pointer = head
        while old_pointer:
            new_pointer.next = old_pointer.next
            old_pointer.next = old_pointer.next.next
            new_pointer = new_pointer.next
            old_pointer = old_pointer.next
        return dummy.next
        

