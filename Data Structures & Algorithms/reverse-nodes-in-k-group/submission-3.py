# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            temp = node
            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            return prev

        def get_node(node, k):
            k -= 1
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        temp = head
        prev_node = None

        while temp:
            kth_node = get_node(temp, k)
            if not kth_node:
                break

            next_node = kth_node.next
            kth_node.next = None  # detach k-group
            new_head = reverse(temp)

            # connect previous group to current
            if prev_node:
                prev_node.next = new_head
            else:
                head = new_head  # first reversed segment

            # move pointers
            last_node = temp  # old head becomes tail after reversal
            last_node.next = next_node
            prev_node = last_node
            temp = next_node

        return head
