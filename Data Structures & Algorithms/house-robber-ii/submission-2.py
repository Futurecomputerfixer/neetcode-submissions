class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        return max(self.rob_r(nums[:N-1]), self.rob_r(nums[1:]))

    def rob_r(self, nums: List[int]) -> int:
        if not nums: return 0
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