# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        n_a, n_b = headA, headB
        len_a, len_b = 1, 1
        if not n_a or not n_b:
            return None
        while n_a.next:
            len_a += 1
            n_a = n_a.next
        while n_b.next:
            len_b += 1
            n_b = n_b.next
        
        if n_b != n_a:
            return None
        (h_long, h_short) = (headA, headB) if len_a > len_b else (headB, headA)
        
        for _ in range(abs(len_a - len_b)):
            h_long = h_long.next
        while h_long != h_short:
            h_long = h_long.next
            h_short = h_short.next
        return h_short
        