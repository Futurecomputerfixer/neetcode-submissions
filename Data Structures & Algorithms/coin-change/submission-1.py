class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        i = 1 
        while i <= amount:
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i-coin]+1
                    dp[i] = min(dp[i],dp[i-coin]+1)
            i+=1
        
        return dp[amount]