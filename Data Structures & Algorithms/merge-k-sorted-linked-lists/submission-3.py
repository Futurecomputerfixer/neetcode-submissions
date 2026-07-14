import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        heap = []
        for i, node in enumerate(lists):
            if not node: continue
            heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            (val, i, node) = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
