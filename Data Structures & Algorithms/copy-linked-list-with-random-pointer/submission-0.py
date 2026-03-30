class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create the copy nodes and interleave them with the original nodes
        temp = head
        while temp:
            copy_node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = copy_node.next

        # Step 2: Set random pointers for the copy nodes
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # Step 3: Separate the copied list from the original list
        temp = head
        dummy = Node(-1)
        copy_curr = dummy
        while temp:
            copy_node = temp.next
            temp.next = copy_node.next
            copy_curr.next = copy_node
            copy_curr = copy_curr.next
            temp = temp.next

        return dummy.next
