class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n 

        def bt(state):
            if len(state) == n:
                res.append(state[:])
            
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    state.append(nums[i])
                    bt(state)

                    used[i] = False
                    state.pop()
            
        
        bt([])
        return res
                