"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        M = {}
        dummy = Node(0)
        curr = head
        prev2 = dummy
        while curr:
            tmp = Node(curr.val)
            M[curr] = tmp
            prev2.next = tmp
            prev2 = prev2.next
            curr = curr.next

        curr = head

        while curr:
            M[curr].random =  M[curr.random] if curr.random else None
            curr = curr.next
        
        return dummy.next


            