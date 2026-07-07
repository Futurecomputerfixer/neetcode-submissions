class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i-1 not in nums:
                temp = 0
                while i in s:
                    temp += 1
                    i += 1
                
                res = max(res, temp)
        
        return res

        
