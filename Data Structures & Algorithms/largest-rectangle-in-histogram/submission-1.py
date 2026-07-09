class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        Max = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                (h, index) = stack.pop()
                Max = max(Max, (i-index)*h)
                start = index
            stack.append((heights[i], start))
        for (h, index) in stack:
            Max = max(Max, (len(heights)-index)*h)
        return Max