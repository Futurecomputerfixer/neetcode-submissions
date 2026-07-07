class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []
        prefix, suffix = [1], [1]
        for i in nums:
            prefix.append(prefix[-1]*i)
        prefix.pop()
        for i in range(len(nums)-1):
            suffix.append(suffix[-1]*nums[len(nums)-1-i])
        
        res = []
        for i in range(len(nums)):
            res.append( prefix[i]* suffix[len(nums)-1-i])

        return res
        
        
