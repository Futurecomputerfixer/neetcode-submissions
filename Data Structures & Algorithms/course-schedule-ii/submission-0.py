class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])

        res = []

        visited = set()
        inPath = set()
        def dfs(num):
            if num in visited: return True
            if num in inPath: return False
            inPath.add(num)

            for c in graph[num]:
                if not dfs(c):
                    return False
            
            inPath.discard(num)
            visited.add(num)
            res.append(num)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res[::-1]
