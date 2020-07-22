# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        dummy_head = ListNode(-1)
        d = dummy_head
        while p and q:
            if p.val < q.val:
                d.next = p
                d = d.next
                n = p.next
                p.next = None
                p = n               
            else:
                d.next = q
                d = d.next
                n = q.next
                q.next = None
                q = n
        d.next = p or q
        return dummy_head.next
    