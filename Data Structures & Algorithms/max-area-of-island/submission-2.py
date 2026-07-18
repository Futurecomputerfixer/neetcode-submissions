class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        n = len(grid)
        m = len(grid[0])
        res = 0

        def dfs(i, j):
            if i >= 0 and i < n and j >= 0 and j < m and (i,j) not in visited and grid[i][j] == 1:
                visited.add((i, j))
                return 1 + dfs(i+1, j)+dfs(i-1, j)+dfs(i, j+1)+dfs(i, j-1)
            else: return 0



        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
        
        return res