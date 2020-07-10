"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flat_util(node):
            if not node:
                return None
            p = node
            while p:
                n = p.next
                if p.child:
                    flat_util(p.child)
                    x = p.child
                    while x.next:
                        x = x.next
                    p.next = p.child
                    p.child = None
                    p.next.prev = p
                    x.next = n
                    if n:
                        n.prev = x
                p = n  
        flat_util(head)
        return head
        