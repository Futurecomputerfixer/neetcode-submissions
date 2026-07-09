class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(l, r):
            if l > r: return -1
            elif l == r: return -1 if nums[l] != target else l
            else:
                m = (l+r) // 2
                return max(recurse(l, m), recurse(m+1, r))
        
        return recurse(0, len(nums)-1)