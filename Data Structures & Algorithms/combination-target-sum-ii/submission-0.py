class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        ans = []
        def bt(state, idx, total):
            if total == target:
                ans.append(state[:])
                return
            elif total > target:
                return
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                if total+ nums[i] > target: break

                state.append(nums[i])
                bt(state, i+1, total+ nums[i])
                state.pop()
        bt([], 0, 0)
        return ans