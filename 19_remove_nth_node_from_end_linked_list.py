# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr1, ptr2 = head, head
        for _ in range(0, n):
            ptr2 = ptr2.next
        
        dummy_node = ListNode()
        dummy_node.next = head
        n = dummy_node
        while ptr2:
            n = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        n.next = ptr1.next
        del ptr1
        return dummy_node.next
        