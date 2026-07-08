class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]

        res = 0

        while l < r:
            if leftMax < rightMax:
                tall = max(leftMax, height[l])
                res += tall - height[l]
                l+=1
                leftMax = max(leftMax, height[l])
            else:
                res += max(rightMax, height[r])- height[r]
                r-=1
                rightMax = max(rightMax, height[r])
        
        return res