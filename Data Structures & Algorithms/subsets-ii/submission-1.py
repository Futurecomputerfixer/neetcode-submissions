class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        def bt(state, idx):
            
            ans.append(state[:])
                
        
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                state.append(nums[i])
                bt(state, i+1)
                state.pop()

        bt([], 0)
        return ans