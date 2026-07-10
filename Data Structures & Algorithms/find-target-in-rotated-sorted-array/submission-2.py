class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r  = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m

        pivot = l
        def real(x): return (x+pivot)%len(nums)



        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2

            if nums[real(m)] == target:
                return real(m)
            elif nums[real(m)] < target:
                l =  m + 1
            else:
                r = m - 1
        
        return -1
