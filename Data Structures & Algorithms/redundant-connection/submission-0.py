class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = defaultdict(int)
        
        def find(x):
            while x in parents:
                x = parents[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            parents[rootY] = rootX

        
        for edge in edges:
            if find(edge[0]) == find(edge[1]): return edge
            union(edge[0], edge[1])