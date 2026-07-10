class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(k):

            return sum([math.ceil(pile/k) for pile in piles]) <= h
        
        while l < r:
            m = (l+r) // 2
            if canEat(m):
                r = m
            else:
                l = m+1
        return l

        