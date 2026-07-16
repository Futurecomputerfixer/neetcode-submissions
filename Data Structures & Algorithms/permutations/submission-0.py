class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        tmp = self.permute(nums[1:])
        el = nums[0]
        res = []

        for L in tmp:
            for i in range(len(L)):
                res.append(L[:i] + [el]+L[i:])
            
            res.append(L+[el])

        return res