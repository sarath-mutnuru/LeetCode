# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def cycle_len(ptr):
            n = 0
            end = ptr
            while True:
                n += 1
                ptr = ptr.next
                if ptr == end:
                    break
            return n
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                c = cycle_len(slow)
                slow, fast = head, head
                for _ in range(c):
                    slow = slow.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        
        
        