from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = 0
        res = []

        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            if dq[0] < l:
                dq.popleft()
            
            if r-l+1 >= k:
                l += 1
                res.append(nums[dq[0]])
        
        return res
            