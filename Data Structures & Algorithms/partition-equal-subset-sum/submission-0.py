class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 == 1: return False
        
        dp = [False]*(S//2 + 1)
        dp[0] = True

        for num in nums:
            for t in range(S//2, num-1, -1):
                dp[t] = dp[t] or dp[t-num]
        
        return dp[-1]
        