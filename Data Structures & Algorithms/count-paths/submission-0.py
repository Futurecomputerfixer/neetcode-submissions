class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up = 0 if i == 0 else dp[i-1][j]
                left = 0 if j == 0 else dp[i][j-1]
                dp[i][j] = up+left
                if i == 0 and j == 0:
                    dp[i][j] = 1
        
        return dp[m-1][n-1]