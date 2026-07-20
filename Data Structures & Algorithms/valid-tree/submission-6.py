class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False

        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue  
                if nei in visited:
                    return False  # found a cycle
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n