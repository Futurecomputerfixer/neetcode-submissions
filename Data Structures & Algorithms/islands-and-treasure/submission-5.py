from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        chests = []
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    chests.append((i,j))

        q = deque(chests)
        visited = set()
        step =  0
        while q:
            level = len(q) 
            for _ in range(level):
                (i, j) = q.popleft()
                if i < 0 or i > n - 1 or j < 0 or j > m - 1: continue
                if grid[i][j] <  0: continue
                if (i, j) in visited: continue
                visited.add((i, j))

                grid[i][j] = min(step, grid[i][j])
                q.append((i+1, j))
                q.append((i-1, j))
                q.append((i, j+1))
                q.append((i, j-1))
            step += 1
                    


