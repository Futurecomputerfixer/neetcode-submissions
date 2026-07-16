class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]

        tmp = self.subsets(nums[1:])

        

        for i in range(len(tmp)):
            tmp.append(tmp[i] + [nums[0]])

        return tmp
