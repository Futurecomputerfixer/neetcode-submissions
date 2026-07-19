from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_starters = [(0, j) for j in range(len(heights[0]))]+[(row+1, 0) for row in range(len(heights)-1)]
        atlantic_starters = [(len(heights)-1, j) for j in range(len(heights[0]))]+[(row, len(heights[0])-1) for row in range(len(heights)-1)]
        pacific = set()
        atlantic = set()

        q = deque(pacific_starters)
        while q:
            for i in range(len(q)):
                (i, j) = q.popleft()
                pacific.add((i, j))
                val = heights[i][j]
                for (r, c) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    idx_i, idx_j = i+r, j+c
                    if idx_i < 0 or idx_i >= len(heights) or idx_j < 0 or idx_j >= len(heights[0]):
                        continue
                    if heights[idx_i][idx_j] < val:
                        continue
                    if (idx_i, idx_j) in pacific:
                        continue
                    q.append((idx_i, idx_j))
        
        q = deque(atlantic_starters)
        while q:
            for _ in range(len(q)):
                (i, j) = q.popleft()
                atlantic.add((i, j))
                val = heights[i][j]
                for (r, c) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    idx_i, idx_j = i+r, j+c
                    if idx_i < 0 or idx_i >= len(heights) or idx_j < 0 or idx_j >= len(heights[0]):
                        continue
                    if heights[idx_i][idx_j] < val:
                        continue
                    if (idx_i, idx_j) in atlantic:
                        continue
                    q.append((idx_i, idx_j))
        
        return list(atlantic & pacific)
        






        