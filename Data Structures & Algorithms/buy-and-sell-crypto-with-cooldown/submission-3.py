class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        hold = [0]*days
        free = [0]*days
        sold = [0]*days

        for i in range(days):
            if i == 0:
                hold[0] = -prices[i]
                continue
            
            hold[i] = max(hold[i-1], free[i-1]- prices[i])
            free[i] = max(free[i-1], sold[i-1])
            sold[i] = hold[i-1] + prices[i]

        
        return max(max(sold), max(free) ,  max(hold) )
