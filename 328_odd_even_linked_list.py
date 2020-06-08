# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        p = head
        head_even, head_odd = None, None
        p_even, p_odd = ListNode(0), ListNode(0)
        is_odd = False
        while p:
            is_odd = not is_odd
            if is_odd:
                if not head_odd:
                    head_odd = p
                else:
                    p_odd.next = p
                p_odd = p
            
            else:
                if not head_even:
                    head_even = p
                else:
                    p_even.next = p
                p_even = p
            p = p.next
                
        p_odd.next = head_even
        p_even.next = None
        return head_odd
            