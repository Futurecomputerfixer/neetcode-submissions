class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0 
        p1, p2 = 0, 0 
        while p2 < len(prices)-1:
            p2 += 1
            if prices[p2] < prices[p1]:
                p1 = p2
            else:
                Max = max(Max, prices[p2] - prices[p1])
        
        return Max