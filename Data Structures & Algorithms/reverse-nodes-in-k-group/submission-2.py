# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head

        for _ in range(k):
            if not node: return head
            node = node.next
        

        prev, curr = None, head

        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        head.next = self.reverseKGroup(curr, k)

        return prev