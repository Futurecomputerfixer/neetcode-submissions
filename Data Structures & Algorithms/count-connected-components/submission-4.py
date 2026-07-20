class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
     
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
