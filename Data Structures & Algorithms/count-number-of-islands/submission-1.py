class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        n = len(grid)
        m = len(grid[0])
        res = 0 

        def dfs(i, j):
            if i >= 0 and i < n and j >= 0 and j < m and (i,j) not in visited and grid[i][j] == '1':
                visited.add((i, j))
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)



        for i in range(n):
            for j in range(m):
                if (i, j) in visited or grid[i][j] == '0': continue
                res += 1
                dfs(i, j)
        
        return res
