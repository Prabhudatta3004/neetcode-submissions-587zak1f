# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        def get_kth_node(head,k):
            temp = head
            k -=1
            while temp and k>0:
                k -=1
                temp = temp.next
            return temp
        
        temp = head
        prev_node = None
        while temp:
            ## get the kth node
            kth_node = get_kth_node(temp,k)
            if not kth_node:
                # do something
                if prev_node:
                    prev_node.next = temp
                break
            ## now store the next_node
            next_node = kth_node.next
            kth_node.next = None
            reverse(temp)

            if temp == head:
                head = kth_node
            else:
                if prev_node:
                    prev_node.next = kth_node
            prev_node = temp
            temp = next_node
        return head