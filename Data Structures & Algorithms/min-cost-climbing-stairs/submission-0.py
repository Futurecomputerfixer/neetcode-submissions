class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, curr = 0, 0
        i = 2
        while i <= n:
            tmp = min(prev+cost[i-2], curr+cost[i-1])
            prev, curr = curr, tmp
            i+=1
        
        return curr