class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def formula(x, y): return math.sqrt((x - 0)**2 + (y - 0)**2)

        heap = []

        for point in points:
            heapq.heappush(heap, (-formula(point[0], point[1]), point[0], point[1]))
            if len(heap) > k: heapq.heappop(heap)
        
        res = []
        while heap:
            val, x, y = heapq.heappop(heap)
            
            res.append([x, y])
        
        return res