# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse_list(head):
            n = head
            temp, prev = [None]*2
            while n:
                temp = n.next
                n.next = prev
                prev = n
                n = temp
            return prev
        
        p, ptr1, ptr2 = head, head, head
        while ptr2 and ptr2.next:
            ptr1, ptr2 = ptr1.next, ptr2.next.next
        
        reversed = reverse_list(ptr1)       
        while reversed and p:
            if p.val != reversed.val:
                return False
            p, reversed = p.next, reversed.next
        return True