# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Steps: 01 to find the middle node
        # Step: 02 to break into two different lists
        ## head>>>middle_element, Middle_element+1>>>tail
        # Step: 03 reverse the second sub-list
        # Step: 04 take the two sublist and weave through it

        fast,slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle_node = slow

        second_head = middle_node.next
        middle_node.next = None

        curr = second_head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_head = prev

        ## 1st sublist : head>>midpoint
        ## 2nd sublist: second_head>>tail

        temp = head
        temp_2 = second_head

        ## temp>temp_2>temp.next

        while temp_2:
            next_1 = temp.next 
            next_2 = temp_2.next
            temp.next = temp_2
            temp_2.next = next_1

            temp = next_1
            temp_2 = next_2


## test case : 1>2>3>4 o/p : 1>4>2>3
## 1>2 , 4>3 , 1>4>2>3