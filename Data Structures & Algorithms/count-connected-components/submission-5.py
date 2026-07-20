class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))

        def find(x):
            while x != parents[x]:
                x = parents[x]
            
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parents[rootY] = rootX
        
        for edge in edges:
            union(edge[0], edge[1])
        
        return sum([1 if parents[i] == i else 0 for i in range(n)])


        