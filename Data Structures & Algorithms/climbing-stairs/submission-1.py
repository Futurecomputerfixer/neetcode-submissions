class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        prev = 1
        curr = 1
        i = 2
        while i <= n:
            tmp = prev+curr
            prev = curr
            curr = tmp
            i+=1
        
        return curr