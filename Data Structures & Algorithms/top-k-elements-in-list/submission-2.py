class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        
        heap = []
        for i in cnt.keys():
            heapq.heappush(heap, (cnt[i], i))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res