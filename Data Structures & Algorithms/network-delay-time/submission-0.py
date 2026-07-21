class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for time in times:
            adj[time[0]].append( [time[1], time[2]])


        heap = []
        distance = [float("inf")] * (n+1)
        distance[k] = 0
        heapq.heappush(heap, (0, k))
        visited = set()

        while heap:
            (dist, node) = heapq.heappop(heap)
            if node in visited: continue
            visited.add(node)
            nbs = adj[node]
            for nb in nbs:
                distance[nb[0]] = min(distance[nb[0]], nb[1]+dist)
                heapq.heappush(heap, (distance[nb[0]], nb[0]))
        if max(distance[1:]) ==  float("inf"): return -1   
        return max(distance[1:])


