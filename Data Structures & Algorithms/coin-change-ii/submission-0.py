class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 1   # one way to make amount 0: use no coins, regardless of which coins are available
        
        for i in range(1, n + 1):
            coin = coins[i - 1]
            for a in range(amount + 1):
                dp[i][a] = dp[i-1][a]                   # don't use this coin type at all
                if a >= coin:
                    dp[i][a] += dp[i][a - coin]          # use at least one of this coin (stay on row i, since reuse is allowed)
        
        return dp[n][amount]