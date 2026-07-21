class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        i = 2
        while i < n:
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            i+=1
        
        return dp[n-1]