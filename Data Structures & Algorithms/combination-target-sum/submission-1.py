class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def bt(state, idx):
            if idx == len(nums):
                return
            if sum(state) == target:
                ans.append(state[:])
                return
            elif sum(state) > target:
                return
            else:
                state.append(nums[idx])
                bt(state, idx)

                state.pop()
                bt(state, idx+1)
        bt([], 0)
        return ans