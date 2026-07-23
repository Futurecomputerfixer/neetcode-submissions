class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]: 
                    dp[j+1][i+1] = dp[j][i]
                else:
                    dp[j+1][i+1] = min(dp[j][i], dp[j+1][i], dp[j][i+1])+1

        return dp[m][n]