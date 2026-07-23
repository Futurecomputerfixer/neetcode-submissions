class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2): text1, text2 = text2, text1
        dp = [[0]*len(text1) for _ in range(len(text2))]

        for j in range(len(text2)):
            for i in range(len(text1)):
                if text1[i] == text2[j]:
                    dp[j][i] = dp[j-1][i-1]+1 if i > 0 and j > 0 else 1
                else:
                    top = dp[j-1][i] if j > 0 else 0
                    left = dp[j][i-1] if i > 0 else 0
                    dp[j][i] = max(top, left)

        
        return dp[-1][-1]